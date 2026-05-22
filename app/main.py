from fastapi import FastAPI
from app.api.routes import analysis, hands, health

app = FastAPI()

app.include_router(analysis.router)
app.include_router(hands.router)
app.include_router(health.router)
