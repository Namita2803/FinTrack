from fastapi import FastAPI

app = FastAPI(
    title="FinTrack API",
    description="Expense Management Backend"
)


@app.get("/")
def home():
    return {
        "message": "FinTrack Backend Running"
    }