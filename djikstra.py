graph = {
        "A": {"B": 5},
        "B": {"A": 5, "C": 5, "F": 1},
        "C": {"B": 5, "D": 5, "E": 5},
        "D": {"C": 5, "F": 1},
        "E": {"C": 5},
        "F": {"B": 1, "D": 1}
    }
cost = {node: 0 for node in graph}
known = [input("Please input a node to start at: ")]
paths = {node: [] for node in graph}

for i in known:
    for neighbour in {k: v for k, v in sorted(graph[i].items(), key=lambda item: item[1])}:
        if neighbour not in known:
            if neighbour not in cost or cost[neighbour] < cost[i] + graph[i][neighbour]:
                cost[neighbour] = cost[i] + graph[i][neighbour]
                paths[neighbour] = [j for j in paths[i]]
                paths[neighbour].append(i)
            known.append(neighbour)

print(paths)
print(known)
print(cost)
