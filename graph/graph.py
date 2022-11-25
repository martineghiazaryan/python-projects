# this the Markov Chain representation

import random 

#defining the graph in terms of vertices

class Vertices:
    def __init__(self, value): # value will be the word
        self.value = value
        self.adjacent = {} # nodes that have an edge from this vertex

        def add_edge_to(self, vertex, weight=0):
            # this is adding an edge to the vertex we input with weight
            self.adjacent[vertex] = weight

        def increment_edge(self, vertex):
            # this is incrementing the weight of the edge
            self.adjacent[vertex] = self.adjacetn.get(vertex, 0) + 1

# now having the vertex representation we put this together into graph

class Graph:
    def __init__(self):
        self.vertices = {}