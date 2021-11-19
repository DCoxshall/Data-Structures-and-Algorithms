import random
import math

example_graph = {"A": {"loc": (5, 4), "B": 2}}

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def generate_graph(n, bi_directional = True, locations = False):
    nodes = [ALPHABET[i] for i in range(n)]

    graph = {node: {"loc": [-1, -1]} for node in nodes}
    
    for i in graph:
        graph[i]["loc"][0] = random.randint(1, 10)
        graph[i]["loc"][1] = random.randint(1, 10)
                

    for node in graph:
        four_closest = {"{": 97, "}": 98, "[": 99, "]": 100, "#": 101} #{node: dist}
        for neighbour in graph:
            furthest_neighbour = max(four_closest, key=four_closest.get)
            if get_distance(graph, node, neighbour) < four_closest[furthest_neighbour]:
                del four_closest[furthest_neighbour]
                four_closest[neighbour] = get_distance(graph, node, neighbour)

        four_closest = {k: v for k, v in sorted(four_closest.items(), key=lambda item: item[1])}
        del four_closest[node]
        closest_nodes = list(four_closest.keys())
        number_of_connections = random.randint(1, 4)
        
        for i in range(0, number_of_connections):
            graph[node][closest_nodes[i]] = math.floor(four_closest[closest_nodes[i]])
            if bi_directional:
                graph[closest_nodes[i]][node] = math.floor(four_closest[closest_nodes[i]])

    if not locations:
        graph = strip_locs(graph)

    return graph

def strip_locs(graph):
    for node in graph:
        del graph[node]["loc"]

    return graph

def get_distance(graph, node1, node2):
    return math.sqrt((graph[node1]["loc"][0] - graph[node2]["loc"][0]) ** 2 + (graph[node1]["loc"][1] - graph[node2]["loc"][1]) ** 2)    
        
def visualise(graph):
    matrix = [['.' for _ in range(11)] for _ in range(11)]
    for node in graph:
        matrix[graph[node]["loc"][0]][graph[node]["loc"][1]] = node

    for i in matrix:
        for j in i:
            print(j, end=' ')
        print()

if __name__ == "__main__":
    g = generate_graph(20, locations = True)
    print(g)
    visualise(g)
