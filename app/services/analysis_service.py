from app.engine.monte_carlo import MonteCarloEngine
from app.engine.recommendation_engine import RecommendationEngine

mc = MonteCarloEngine()
recommender = RecommendationEngine()

def analyze_spot(request):

   equity = mc.simulate(
       hero_hand=request.hero_cards,
       board=request.board
   )

   recommendation = recommender.recommend(equity)

   return {
       "equity": equity,
       "recommendation": recommendation,
       "played_action": request.actions[-1].action,
       "ev_comment": "Potential EV loss detected"
   }
