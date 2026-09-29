FROM python:3.11-slim
WORKDIR /app
COPY pyproject.toml uv.lock ./
COPY packages ./packages
RUN pip install --no-cache-dir uv && uv sync --locked --no-dev
EXPOSE 8501
CMD ["uv", "run", "streamlit", "run", "packages/synapse-ui/src/synapse_ui/app.py", "--server.address=0.0.0.0", "--server.port=8501"]
