from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes.analysis import router as analysis_router
from app.api.routes.hands import router as hands_router

app = FastAPI(
    title="Poker Analysis API",
    version="1.0.0"
)

# ⭐ CORS — required for GitHub Codespaces
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          # Allow your frontend URL or "*" for dev
    allow_credentials=True,
    allow_methods=["*"],          # Allow POST, GET, etc.
    allow_headers=["*"],          # Allow JSON headers
)

# ⭐ Include your routers
app.include_router(
    analysis_router,
    tags=["Analysis"]
)

app.include_router(
    hands_router,
    tags=["Hands"]
)

# ⭐ Root endpoint
@app.get("/")
async def root():
    return {"message": "Poker Analysis API Running"}