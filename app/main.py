from fastapi import FastAPI
from app.api.routes.analysis import router as analysis_router

app = FastAPI(title="Poker Analysis API")

app.include_router(
   analysis_router,
   prefix="/analysis",
   tags=["Analysis"]
)

@app.get("/")
def health():
   return {"status": "running"}
