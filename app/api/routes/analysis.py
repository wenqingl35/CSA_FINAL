@router.post("/analyze")
async def analyze_hand(request: AnalysisRequest):

    return analysis_service.analyze(request)
