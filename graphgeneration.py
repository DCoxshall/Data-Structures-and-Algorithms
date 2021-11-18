# Program generates a graph with n elements, with each element having
# between 1 and 3 connections inclusive.
#
# Graphs are represented by dictionaries within dictionaries, in the form
# {a: {b: z, c: y}} where a, b, and c are elements and z and y are one-way
# connections to b and c from a. 

import random

def generateGraph(n) -> dict:
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    graph = {alphabet[i]: {} for i in range(n)}
    nodes = list(graph.keys())
    #for i in graph:
    print(nodes)
    print(graph)

    for i in graph:
        temp_nodes = nodes
        for i in range(random.randint(0, 4)):
            node = random.choice(temp_nodes)
            
        
        
generateGraph(5)
