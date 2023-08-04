import numpy as np
import os

from backend.utils import Graph


def solve(universe:Graph, day:int, planet:str, autonomy:int,
          k:int, empire: dict, millenium_falcon:dict, ANSWER:dict) -> None :
    """
     Compute the odds that Millennium Falcon reaches the final planet in time and saves the galaxy. 
     It is based on DFS algorithm
     
     Parameters
     ----------
     universe: Graph
         The graph representing the universe.
     day: int
         The day Millenium Falcon appears on the planet.
     planet: int
         The planet where Millenium Falcon is currently.
    autonomy: int
        Remaining fuel of Millenium Falcon.
    k: int
        Number of times Millenium Falcon encountered the bounty hunters.
    empire: dict
        The empire data.
    millenium_facon: dict
        the Millenium falcon data
    ANSWER: dict[str:double]
        Dictionary of one item which maps odds to its value.'
          
    """
    
    if day > empire["countdown"] or autonomy < 0 :
        return 
    
    is_enemy_here = ({"planet": planet, "day": day} in empire["bounty_hunters"])
    k += is_enemy_here
    
    if planet == millenium_falcon["arrival"] :
        ANSWER['odds'] = max(ANSWER['odds'], 1 - np.sum(np.array([1 / 10 * (9 / 10)**i for i in range(k)])))
        return
    
    # Option 1: Stay at the current planet     
    solve(universe,day+1, planet, millenium_falcon["autonomy"], k, empire, millenium_falcon, ANSWER)
    
   
    for (neighbour, duration_days) in universe.get_neighbors(planet) :
         # Option 2: Travel to a neighboring planet
        solve(universe, day + duration_days, neighbour, autonomy - duration_days, k, empire, millenium_falcon, ANSWER)
        
    return 
                         