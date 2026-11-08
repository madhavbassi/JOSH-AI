FROM node:20-alpine AS frontend-build
WORKDIR /app/frontend
COPY frontend/package.json frontend/package-lock.json ./
RUN npm ci
COPY frontend/ ./
ARG VITE_CHAT_API_URL=/chat
ARG VITE_RESUME_URL=/resume
ARG VITE_TTS_API_URL=/tts
ARG VITE_ENABLE_VOICE_GREETING=false
ENV VITE_CHAT_API_URL=${VITE_CHAT_API_URL} \
    VITE_RESUME_URL=${VITE_RESUME_URL} \
    VITE_TTS_API_URL=${VITE_TTS_API_URL} \
    VITE_ENABLE_VOICE_GREETING=${VITE_ENABLE_VOICE_GREETING}
RUN npm run build

FROM python:3.11-slim AS app
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1
RUN apt-get update \
    && apt-get install -y --no-install-recommends libgomp1 \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY pyproject.toml uv.lock ./
RUN pip install --no-cache-dir uv \
    && uv sync --frozen --no-dev \
    && rm -rf /root/.cache/uv
ENV PATH="/app/.venv/bin:${PATH}"
COPY backend/ ./backend/
COPY --from=frontend-build /app/frontend/dist ./frontend/dist
EXPOSE 8000
CMD ["sh", "-c", "uvicorn backend.main:app --host 0.0.0.0 --port ${PORT:-8000}"]
