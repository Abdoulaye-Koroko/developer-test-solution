import numpy as np

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