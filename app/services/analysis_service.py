from app.ai.coaching_engine import CoachingEngine 
from app.engine.recommendation_engine import RecommendationEngine

mc = CoachingEngine()
recommender = RecommendationEngine()

async def analyze_spot(request: dict):

   # 1. Call the correct, existing async method using 'await'
   engine_result = await mc.analyze_hand(request)

   # 2. Check if the AI analysis succeeded
   if not engine_result.get("success"):
       return {
           "success": False,
           "error": engine_result.get("error", "AI Analysis failed")
       }

   # Extract the parsed AI response data
   ai_data = engine_result.get("data", {})
   equity = ai_data.get("estimated_equity", 0.50)

   # 3. Pass the extracted equity to your recommendation engine
   recommendation = recommender.recommend(equity)

   # 4. Safely read action history
   actions = request.get('action_history', [])
   played_action = actions[-1].get('action') if actions else "None"

   # Return the combined response back to the route
   return {
       "equity": equity,
       "recommendation": recommendation,
       "played_action": played_action,
       "ai_coaching": ai_data  # Includes full JSON response from the updated prompt
   }