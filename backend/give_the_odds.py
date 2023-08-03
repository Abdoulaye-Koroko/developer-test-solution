#!/usr/bin/env python


import sys
import os

from backend.utils import read_json_file
from backend.algorithm import solve
from backend.utils import build_universe



def main(path_to_empire:str, path_to_falcon_millenimum:str) -> None:
    """
    The main function. Prints the chance that Millenium Falcon arrives at destination
    at time.
    
    Parameters:
    -----------
    path_to_empire: str
        Path towards empire json file.
    path_to_falcon_millenium: str
        Path towards Falcon Millenium json file
    """
    try:
        empire = read_json_file(path_to_empire)
        falcon_millenium = read_json_file(path_to_falcon_millenimum)
        db_path = falcon_millenium["routes_db"]
        db_path = os.path.join(os.path.split(path_to_falcon_millenimum)[0],db_path)
        table_name = 'ROUTES'
        universe = build_universe(db_path,table_name)
        assert type(falcon_millenium)==dict
        assert type(empire)==dict
    except:
        print("Encountered a problem when loading data. Make sure that you correctly set the paths towards the two files or both of the files are valid.")
        return 
        
    day = 0 
    ANSWER = {'odds' : 0}
    departure = falcon_millenium['departure']
    autonomy = falcon_millenium['autonomy']
    k = 0
    solve(universe,day, departure, autonomy, k, empire, falcon_millenium, ANSWER)
    odds = ANSWER['odds']
    print(f" Millennium Falcon has {odds*100:.2f}% chance to reache {falcon_millenium['arrival']} in time and saves the galaxy.")
    
    return 

        
    

if __name__ == "__main__":

    if len(sys.argv) != 3:
         print("Make sure that you correctly set the paths towards the two files. Usage: python backend/main.py /path/to/millenium_facon.json /path/to/empire.json ")
    else:
        path_to_falcon_millenimum = os.path.abspath(sys.argv[1])
        path_to_empire = os.path.abspath(sys.argv[2])
        main(path_to_empire, path_to_falcon_millenimum)


    

    
    



