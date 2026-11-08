# JOSH — Personal AI Assistant

JOSH is a React/Vite frontend and FastAPI backend for a personal assistant. The backend retrieves relevant profile information from `backend/knowledge_base.py` and generates grounded answers through Groq.

## Run locally

Requirements: Python 3.11+, Node.js 20+, and npm.

1. Create a virtual environment and install backend dependencies:

   ```sh
   python -m venv .venv
   source .venv/bin/activate
   pip install -r backend/requirements.txt
   ```

2. Set `GROQ_API_KEY` in your shell or a root `.env` file (copy `.env.example` and edit it).
3. Start the backend from the repository root:

   ```sh
   uvicorn backend.main:app --reload --port 8000
   ```

4. In another terminal, start the frontend:

   ```sh
   cd frontend
   npm ci
   cp .env.example .env.local
   npm run dev
   ```

The default development frontend config sends chat to `http://localhost:8000/chat` and loads the resume from `http://localhost:8000/resume`. The backend allows Vite's localhost origins. The embedding model downloads from Hugging Face on the first chat request; that first request can take longer.

## Deploy with Docker

Build and run the combined app so the frontend and API share one origin:

```sh
docker build -t josh .
docker run --rm -p 8000:8000 -e GROQ_API_KEY='your-key' josh
```

Open `http://localhost:8000`. Configure `GROQ_API_KEY` as a secret environment variable in the hosting provider. The container listens on `$PORT` when provided by the host. Chat, health, and resume endpoints are `/chat`, `/health`, and `/resume`.

Voice greeting is optional and disabled by default. To build it in, pass `--build-arg VITE_ENABLE_VOICE_GREETING=true` and set `ELEVENLABS_API_KEY` and `ELEVENLABS_VOICE_ID` as runtime secrets. Do not pass secrets as Docker build args.

For separate frontend and backend hosting, set frontend build variables `VITE_CHAT_API_URL`, `VITE_RESUME_URL`, and (if enabled) `VITE_TTS_API_URL` to the public backend URLs. Set backend `CORS_ORIGINS` to the exact comma-separated frontend origins. Keep `GROQ_API_KEY` only on the backend.

## Project structure

- `frontend/`: responsive React application.
- `backend/main.py`: FastAPI endpoints and static frontend serving in the Docker deployment.
- `backend/rag.py`: lazily initialized embeddings, retrieval, and Groq response generation.
- `backend/knowledge_base.py`: assistant knowledge source.
- `backend/Resume.pdf`: resume served at `/resume`.

The RAG model and embeddings load only on the first chat request; importing the app does not make external API calls. Embeddings are computed for the same chunks used by retrieval.
