# Program generates a graph with n elements, with each element having
# between 1 and 3 connections inclusive.
#
# Graphs are represented by dictionaries within dictionaries, in the form
# {a: {b: z, c: y}} where a, b, and c are elements and z and y are one-way
# connections to b and c from a.

import random


def generate_graph(n, bi_directional=True):
    nodes = get_nodes(n)
    graph = {node: {} for node in nodes}
    three_connections = []
    x = 0
    while (True):
        possible_current_nodes = [
            i for i in nodes if i not in three_connections]
        if possible_current_nodes == []:
            break

        current_node = random.choice(possible_current_nodes)

        possible_connections = [
            i for i in nodes if i not in three_connections and i != current_node]

        if (possible_connections == []):
            break
        connecting_node = random.choice(possible_connections)

        graph = connect_nodes(graph, current_node,
                              connecting_node, bi_directional)

        if len(graph[current_node]) == 3:
            three_connections.append(current_node)
        if len(graph[connecting_node]) == 3:
            three_connections.append(connecting_node)

    return graph


def connect_nodes(graph, current_node, connecting_node, bi_directional):
    weight = random.randrange(1, 21)
    graph[current_node][connecting_node] = weight
    if bi_directional:
        graph[connecting_node][current_node] = weight
    return graph


def get_nodes(n):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    nodes = []
    i = 0
    j = -1
    for _ in range(n):
        if j == -1:
            nodes.append(alphabet[i])
        else:
            nodes.append(alphabet[j] + alphabet[i])
        i += 1
        if i == 26:
            i = 0
            j += 1

    return nodes


if __name__ == "__main__":
    for i in range(100):
        print(generate_graph(5))

# Every node should have at least one connection
# No node should have more than 3 connections coming and 3 connections going
