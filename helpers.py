import math
import psycopg2
from config import config
class Helpers:

    #  Calcualtes the level 
    def levelCalculator(self, level):        
        # 6(n^3)/5 - 15(n^2) + 100n - 140
        print(level)
        levelrate = ((6 * pow(level,3)) / 5) - (15 * pow(level,2)) + (100 * level) - 140
        return math.floor(levelrate)
    
    # Check if the Player has gained a level
    def checkIfPlayerLeveledUp(self, discord_id, plvl, exp):
        if exp >= self.levelCalculator(plvl+1):
            return True
        return False
