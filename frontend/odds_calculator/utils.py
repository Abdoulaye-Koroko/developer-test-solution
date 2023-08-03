import numpy as np
import os 
from backend.utils import read_json_file
from backend.algorithm import solve
from backend.utils import build_universe

def calculate_odds(empire_data):
    """
    Return the chance that Millenium Falcon arrives at destination in time
    based on uploded JSON file.
    
    Paramters
    ---------
    empire_data: dict
        Data from uploaded JSON file.
    
    Returns
    -------
    old: int
        Chance in percentage that  Millenium Falcon arrives at destination in time.
    """
    empire = empire_data
    path_to_falcon_millenimum = os.path.abspath("../examples/example1/millennium-falcon.json")
    falcon_millenium = read_json_file(path_to_falcon_millenimum)
    db_path = falcon_millenium["routes_db"]
    db_path = os.path.join(os.path.split(path_to_falcon_millenimum)[0],db_path)
    table_name = 'ROUTES'
    universe = build_universe(db_path,table_name)
    day = 0 
    ANSWER = {'odds' : 0}
    departure = falcon_millenium['departure']
    autonomy = falcon_millenium['autonomy']
    k = 0
    solve(universe,day, departure, autonomy, k, empire, falcon_millenium, ANSWER)
    
    odds = ANSWER['odds']
    
    return float(f"{odds*100:.2f}")