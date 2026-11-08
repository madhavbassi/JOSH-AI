
import os
import traceback
import json
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, Response
from pydantic import BaseModel, Field
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from .rag import retrieve, ask_llm


# --------------------------------------------------
# 1. LOAD ENVIRONMENT VARIABLES
# --------------------------------------------------

load_dotenv()

ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
ELEVENLABS_VOICE_ID = os.getenv("ELEVENLABS_VOICE_ID")


# --------------------------------------------------
# 2. INITIALIZE APPLICATION
# --------------------------------------------------

app = FastAPI(
    title="JOSH - Personal AI Assistant",
    description="Madhav's personal professional AI assistant",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:5175",
        "http://127.0.0.1:5175",
        "http://localhost:5176",
        "http://127.0.0.1:5176",
        *[origin.strip() for origin in os.getenv("CORS_ORIGINS", "").split(",") if origin.strip()],
    ],
    # Vite increments its port when another local dev server already uses 5173.
    allow_origin_regex=r"https?://(localhost|127\.0\.0\.1)(:\d+)?",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# --------------------------------------------------
# 3. REQUEST MODELS
# --------------------------------------------------

class ChatRequest(BaseModel):
    question: str = Field(
        min_length=1,
        max_length=1000
    )


class VoiceRequest(BaseModel):
    text: str = Field(
        min_length=1,
        max_length=2000
    )


# --------------------------------------------------
# 4. HOME ENDPOINT
# --------------------------------------------------

@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/resume")
def resume():
    resume_path = Path(__file__).with_name("Resume.pdf")
    if not resume_path.is_file():
        raise HTTPException(status_code=404, detail="Resume PDF is unavailable.")
    return FileResponse(resume_path, media_type="application/pdf", filename="Madhav-Bassi-Resume.pdf")


# --------------------------------------------------
# 5. CHAT ENDPOINT (RAG + GROQ)
# --------------------------------------------------

@app.post("/chat")
def chat(request: ChatRequest):

    query = request.question.strip()

    if not query:
        raise HTTPException(
            status_code=400,
            detail="Question cannot be empty."
        )

    try:
        # Retrieve relevant knowledge chunks
        retrieved_chunks = retrieve(
            query,
            top_k=4
        )

        # Combine retrieved chunks into context
        context = "\n\n".join(
            chunk["text"]
            for chunk in retrieved_chunks
        )

        # Generate answer using Groq
        answer = ask_llm(
            query,
            context
        )

        return {
            "answer": answer,
            "sources": list(set(
                chunk["section"]
                for chunk in retrieved_chunks
            ))
        }

    except Exception:
        print("\n========== CHAT ERROR ==========")
        traceback.print_exc()
        print("================================\n")

        raise HTTPException(
            status_code=500,
            detail="Could not generate a chat response."
        )


# --------------------------------------------------
# 6. TEXT-TO-SPEECH ENDPOINT (ELEVENLABS)
# --------------------------------------------------


@app.post("/tts")
def text_to_speech(request: VoiceRequest):

    if not ELEVENLABS_API_KEY:
        raise HTTPException(status_code=500, detail="ELEVENLABS_API_KEY missing")

    if not ELEVENLABS_VOICE_ID:
        raise HTTPException(status_code=500, detail="ELEVENLABS_VOICE_ID missing")

    try:
        print("\n========== TTS DEBUG START ==========")
        print("Voice ID configured:", bool(ELEVENLABS_VOICE_ID))
        print("API key configured:", bool(ELEVENLABS_API_KEY))

        api_request = Request(
            f"https://api.elevenlabs.io/v1/text-to-speech/{ELEVENLABS_VOICE_ID}",
            data=json.dumps({
                "text": request.text.strip(),
                "model_id": "eleven_multilingual_v2",
            }).encode("utf-8"),
            headers={
                "xi-api-key": ELEVENLABS_API_KEY,
                "Content-Type": "application/json",
                "Accept": "audio/mpeg",
            },
            method="POST",
        )
        with urlopen(api_request, timeout=60) as response:
            audio_bytes = response.read()

        print("Audio bytes generated:", len(audio_bytes))
        print("========== TTS DEBUG SUCCESS ==========\n")

        return Response(content=audio_bytes, media_type="audio/mpeg")

    except (HTTPError, URLError, TimeoutError, OSError, ValueError) as e:
        print("\n========== TTS DEBUG FAILED ==========")
        print("Exception:", type(e).__name__)
        print("Message:", str(e))
        print("Status code:", getattr(e, "status_code", None))
        print("Body:", getattr(e, "body", None))
        traceback.print_exc()
        print("========== TTS DEBUG END ==========\n")

        raise HTTPException(
            status_code=502,
            detail="ElevenLabs speech generation failed. Check backend terminal."
        )


# The production image serves the built SPA and API from one origin.
frontend_dist = Path(os.getenv("FRONTEND_DIST_DIR", Path(__file__).parents[1] / "frontend" / "dist"))
if frontend_dist.is_dir():
    app.mount("/", StaticFiles(directory=frontend_dist, html=True), name="frontend")
