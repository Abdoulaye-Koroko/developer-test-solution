import numpy as np
import json
import sqlite3
from typing import Dict, List,Tuple

class Graph:
    """Class for building a graph that represents the universe. The graph is reprented as dictionary 
     where keys are planets and values are lists of neighboring planets and contain tuples of two elements where
     first elemnt is a neighboring planet and the second one is the travel time from the key planet to that planet.
     
     Example:
     {'Tatooine': [('Dagobah', 6), ('Hoth', 6)],
     'Dagobah': [('Tatooine', 6), ('Endor', 4), ('Hoth', 1)],
     'Endor': [('Dagobah', 4), ('Hoth', 1)],
     'Hoth': [('Dagobah', 1), ('Endor', 1), ('Tatooine', 6)]} 
    """   
    def __init__(self):
        self.graph_dict = {}

    def add_vertex(self, vertex:str) -> None:
        """Add a planet to the graph.

        Parameters
        ----------
        vertex : str
            Name of planet.
        """ 
        if vertex not in self.graph_dict:
            self.graph_dict[vertex] = []

    def add_edge(self, vertex1:str, vertex2:str, weight:int) -> None:
        """Add a connexion between two planets.

        Parameters
        ----------
        vertex1 : str
            Name of planet 1.
        vertex2: str
            Name of planet 2.
        
        weight: int
            Travel time from planet 1 to planet 2 and vice versa.
        """
        if vertex1 not in self.graph_dict :
            self.add_vertex(vertex1)
        if vertex2 not in self.graph_dict :
            self.add_vertex(vertex2)
        self.graph_dict[vertex1].append((vertex2, weight))
        self.graph_dict[vertex2].append((vertex1, weight)) 

    def get_neighbors(self, vertex:str) -> List[Tuple]:
        """Get the neighbor of input planet.
        Parameters
        ----------
        vertex : str
            Name of planet.
        
        Returns
        -------
        self.graph_dict[vertex] : list
            List of neighboring planets.
        """
        if vertex in self.graph_dict:
            return self.graph_dict[vertex]
        else:
            return []

    def __str__(self):
        return str(self.graph_dict)
    

def fetch_data_from_database(db_path:str, table_name:str) -> List[Tuple]:
    """Read the sqlite database and return a list containing
     all the routes in the table ROUTES.

        Parameters
        ----------
        db_path : str
            Path towards the sqlite database
        table_name : str
            Name of the table (here ROUTES)

        Returns
        -------
        validated_rows : list
            list of all rows in the table ROUTES.
    """
    try:
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        # Fetch data from the specified table
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()

        # Validate the data
        validated_rows = []
        for row in rows:
            first_col, second_col, third_col = row
            if first_col is None or not first_col.strip():
                raise ValueError("Elements of the first column cannot be null or empty.")
            if second_col is None or not second_col.strip():
                raise ValueError("Elements of the second column cannot be null or empty.")
            if third_col <= 0:
                raise ValueError("Elements of the third column must be strictly positive.")

            validated_rows.append(row)

        # Return the list of tuples
        return validated_rows

    except sqlite3.Error as e:
        print(f"Error accessing database: {e}")
    except ValueError as ve:
        print(f"Data validation error: {ve}")
    finally:
        if connection:
            connection.close()

            

def read_json_file(file_path:str) -> dict:
    """
    Read json file and return the data
    
    Parameters
    ----------
    file_path: str
        Path towards the json file.
    
    Returns
    -------
    data: dict
        data contained in the json file
    
    """
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            return data

    except FileNotFoundError:
        print(f"Error: File not found at '{file_path}'.")
    except json.JSONDecodeError as e:
        print(f"Error: JSON decoding failed - {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


def build_universe(db_path:str,table_name:str):
    """
    Build and return the graph representing the universe.
    
    Parameters
    ---------
    db_path: str
        Path towards the sqlite database
    table_name: str
        Name of the table
        
    Returns
    -------
    universe: Graph
        Graph reprenting the universe.
    
    """
    universe = Graph()
    routes = fetch_data_from_database(db_path, table_name)
    for route in routes:
        vertex1, vertex2, weight = route
        universe.add_edge(vertex1, vertex2, weight)
    return universe
    