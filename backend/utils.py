import numpy as np
import json
import sqlite3

class Graph:
    def __init__(self):
        self.graph_dict = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph_dict:
            self.graph_dict[vertex] = []

    def add_edge(self, vertex1, vertex2, weight):
        if vertex1 not in self.graph_dict :
            self.add_vertex(vertex1)
        if vertex2 not in self.graph_dict :
            self.add_vertex(vertex2)
        self.graph_dict[vertex1].append((vertex2, weight))
        self.graph_dict[vertex2].append((vertex1, weight)) 

    def get_neighbors(self, vertex):
        if vertex in self.graph_dict:
            return self.graph_dict[vertex]
        else:
            return []

    def __str__(self):
        return str(self.graph_dict)
    

def fetch_data_from_database(db_path, table_name):
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

            


def read_json_file(file_path):
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


def build_universe(db_path,table_name):
    universe = Graph()
    routes = fetch_data_from_database(db_path, table_name)
    for route in routes:
        vertex1, vertex2, weight = route
        universe.add_edge(vertex1, vertex2, weight)
    return universe
    