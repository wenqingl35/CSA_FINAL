from fastapi import FastAPI

from app.api.routes.analysis import router as analysis_router
from app.api.routes.hands import router as hands_router

app = FastAPI(
    title="Poker Analysis API",
    version="1.0.0"
)

app.include_router(
    analysis_router,
    tags=["Analysis"]
)

app.include_router(
    hands_router,
    tags=["Hands"]
)


@app.get("/")
async def root():
    return {
        "message": "Poker Analysis API Running"
    }