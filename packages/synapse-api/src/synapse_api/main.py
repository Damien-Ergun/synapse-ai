from fastapi import FastAPI

app = FastAPI(title="Synapse AI V0", docs_url=None, redoc_url=None)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "scope": "week1-health-only"}
