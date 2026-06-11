from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Welcome to FinTrack API"
    }


@app.get("/health")
def health():
    return {
        "status": "Backend running successfully"
    }