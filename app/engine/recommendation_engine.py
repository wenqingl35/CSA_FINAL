class RecommendationEngine:

   def recommend(self, equity: float):

       if equity > 0.7:
           return {
               "action": "raise",
               "size": "75% pot"
           }

       if equity > 0.45:
           return {
               "action": "call"
           }

       return {
           "action": "fold"
       }
