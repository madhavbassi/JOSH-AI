# JOSH frontend

This is the React/Vite UI for the full JOSH app. For local setup, backend configuration, and Docker deployment, see the repository [README](../README.md).

The frontend reads `VITE_CHAT_API_URL`, `VITE_CHAT_REQUEST_FIELD`, `VITE_CHAT_RESPONSE_FIELD`, `VITE_RESUME_URL`, `VITE_TTS_API_URL`, and `VITE_ENABLE_VOICE_GREETING` from its build environment. `frontend/.env.example` shows the local development values. The combined Docker image uses same-origin `/chat` and `/resume` endpoints by default.
