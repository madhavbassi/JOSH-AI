"""Retrieval augmented generation helpers for JOSH."""

import os
import re
from functools import lru_cache

import numpy as np
from dotenv import load_dotenv
from groq import Groq
from sentence_transformers import SentenceTransformer

from .knowledge_base import documents

load_dotenv()
GROQ_MODEL = os.getenv("GROQ_MODEL", "openai/gpt-oss-120b")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "all-MiniLM-L6-v2")
MAX_CHUNK_TOKENS = 200
CHUNK_OVERLAP = 25


def is_heading(line):
    line = re.sub(r"&#x[0-9a-fA-F]+;?", "", line)
    line = re.sub(r"^[^A-Za-z]+", "", line).strip()
    if not line or len(line) > 110:
        return False
    letters = [char for char in line if char.isalpha()]
    return len(letters) >= 6 and sum(c.isupper() for c in letters) / len(letters) >= 0.85


def split_into_sections(text):
    sections = []
    current_title = "General Information"
    current_content = []
    for line in text.splitlines():
        if is_heading(line):
            content = "\n".join(current_content).strip()
            if content:
                sections.append({"title": current_title, "content": content})
            current_title = re.sub(r"&#x[0-9a-fA-F]+;?", "", line)
            current_title = re.sub(r"^[^A-Za-z]+", "", current_title).strip()
            current_content = []
        else:
            current_content.append(line)
    content = "\n".join(current_content).strip()
    if content:
        sections.append({"title": current_title, "content": content})
    return sections


def split_section_into_chunks(title, content, tokenizer):
    prefix = f"Section: {title}\n"
    prefix_tokens = tokenizer.encode(prefix, add_special_tokens=False)
    content_tokens = tokenizer.encode(content, add_special_tokens=False)
    chunk_size = MAX_CHUNK_TOKENS - len(prefix_tokens) - 2
    if chunk_size <= CHUNK_OVERLAP:
        raise ValueError(f"Section title is too long to chunk: {title}")
    chunks = []
    step = chunk_size - CHUNK_OVERLAP
    for start in range(0, len(content_tokens), step):
        token_slice = content_tokens[start : start + chunk_size]
        chunk_content = tokenizer.decode(token_slice, skip_special_tokens=True).strip()
        if chunk_content:
            chunks.append({"section": title, "text": prefix + chunk_content})
        if start + chunk_size >= len(content_tokens):
            break
    return chunks


def create_chunks(raw_documents, tokenizer):
    chunks = []
    for raw_document in raw_documents:
        for section in split_into_sections(raw_document):
            chunks.extend(
                split_section_into_chunks(section["title"], section["content"], tokenizer)
            )
    return chunks


@lru_cache(maxsize=1)
def _knowledge_index():
    """Load the embedding model and index only when the first chat arrives."""
    model = SentenceTransformer(EMBEDDING_MODEL)
    chunks = create_chunks(documents, model.tokenizer)
    if not chunks:
        raise RuntimeError("No knowledge chunks were created.")
    embeddings = model.encode(
        [chunk["text"] for chunk in chunks],
        convert_to_numpy=True,
        normalize_embeddings=True,
        show_progress_bar=False,
    )
    return model, chunks, embeddings


def retrieve(query, top_k=4):
    model, chunks, embeddings = _knowledge_index()
    query_embedding = model.encode(
        query,
        convert_to_numpy=True,
        normalize_embeddings=True,
        show_progress_bar=False,
    )
    scores = np.dot(embeddings, query_embedding)
    return [
        {
            "score": float(scores[index]),
            "section": chunks[index]["section"],
            "text": chunks[index]["text"],
        }
        for index in np.argsort(scores)[::-1][:top_k]
    ]


def ask_llm(question, context):
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise RuntimeError("GROQ_API_KEY is not configured.")
    client = Groq(api_key=api_key)
    response = client.chat.completions.create(
        model=GROQ_MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "Answer concisely using only the supplied context. If the context "
                    "does not contain the answer, say you do not know.\n\n"
                    f"Context:\n{context}"
                ),
            },
            {"role": "user", "content": question},
        ],
    )
    return response.choices[0].message.content or "I could not generate an answer."
