# Program generates a graph with n elements, with each element having
# between 1 and 3 connections inclusive.
#
# Graphs are represented by dictionaries within dictionaries, in the form
# {a: {b: z, c: y}} where a, b, and c are elements and z and y are one-way
# connections to b and c from a. 

def generateGraph(n, bi_directional = True) -> dict:
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    graph = {alphabet[i]: {} for i in range(n)}

    graph = connect_nodes(graph, "C", "D", 10, bi_directional)
    
    print(graph)

def connect_nodes(graph, a, b, weight, bi_directional = True):
    graph[a][b] = weight
    if bi_directional:
        graph[b][a] = weight
    return graph
    
generateGraph(5, True)
