from fastapi import FastAPI

app = FastAPI(title="Consulting Platform API")

@app.get("/health")
async def health():
    return {"status": "ok"}
