FROM python:3.11-slim
WORKDIR /app
COPY pyproject.toml uv.lock ./
COPY packages ./packages
RUN pip install --no-cache-dir uv && uv sync --locked --no-dev
EXPOSE 8000
CMD ["uv", "run", "--no-sync", "uvicorn", "synapse_api.main:app", "--host", "0.0.0.0", "--port", "8000"]
