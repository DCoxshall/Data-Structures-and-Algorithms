# A hypergraph is a generalisation of a graph, where instead of joining two nodes,
# an edge can connect an arbitrary number of nodes

# An edge should be a tuple containing characters as references to nodes, e.g. the edge connecting A, B, and C should be notated as ("A", "B", "C")
class Hypergraph:
    def __init__(self) -> None:
        self.nodes = {}
        self.edges = {}


class Edge:
    def __init__(self) -> None:
        self.
