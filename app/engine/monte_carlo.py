import random

class MonteCarloEngine:

   def simulate(self, hero_hand, board, iterations=10000):

       wins = 0

       for _ in range(iterations):

           villain_strength = random.random()
           hero_strength = random.random()

           if hero_strength > villain_strength:
               wins += 1

       return wins / iterations
