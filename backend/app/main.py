from fastapi import FastAPI

from app.database import engine
from app import models
from app.routes import expenses


models.Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="FinTrack API"
)


app.include_router(expenses.router)


@app.get("/")
def home():

    return {
        "message": "Database Connected"
    }