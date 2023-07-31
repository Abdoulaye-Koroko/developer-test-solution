import numpy as np
import os

from utils import build_universe

def solve(day, planet, autonomy, k, empire, millenium_falcon, ANSWER) :
    
    db_path = os.path.abspath(millenium_falcon["routes_db"])
    table_name = 'ROUTES'
    universe = build_universe(db_path,table_name)
    
    if day > empire["countdown"] or autonomy < 0 :
        return 
    
    is_enemy_here = ({"planet": planet, "day": day} in empire["bounty_hunters"])
    k += is_enemy_here
    
    if planet == millenium_falcon["arrival"] :
       
        ANSWER['probability'] = max(ANSWER['probability'], 1 - np.sum(np.array([1 / 10 * (9 / 10)**i for i in range(k)])))
        return
        
    #solve(day + 1, planet, millenium_falcon_json["autonomy"], k, ANSWER) 
    solve(day+1, planet,  millenium_falcon["autonomy"], k, empire, millenium_falcon, ANSWER)
    for (neighbour, duration_days) in universe.get_neighbors(planet) :
        #solve(day + duration_days, neighbour, autonomy - duration_days, k, ANSWER)
        solve(day + duration_days, neighbour,  autonomy - duration_days, k, empire, millenium_falcon, ANSWER)
        
    return 
                         