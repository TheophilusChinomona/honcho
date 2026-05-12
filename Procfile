# Procfile — process definitions for production deployment
# Used by: Docker, Fly.io, Railway, Heroku, etc.
#
# Usage:
#   uv run gunicorn src.main:app -k uvicorn.workers.UvicornWorker
#   uv run python -m src.deriver

web: uv run fastapi run --host 0.0.0.0 --port $PORT src/main.py
deriver: uv run python -m src.deriver
