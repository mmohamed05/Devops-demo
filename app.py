from fastapi import FastAPI

app = FastAPI(title="DevOps Demo", version="0.1.0")

@app.get("/")
def home():
    return {"message": "Hello, world! DevOps is live!"}

@app.get("/healthz")
def health():
    return {"status": "ok"}
