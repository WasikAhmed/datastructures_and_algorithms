class Graph:
    def __init__(self, directed=False, weighted=False):
        self.graph = {}
        self.directed = directed
        self.weighted = weighted

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = {}

    def add_edge(self, node1, node2, weight=None):
        if not self.weighted:
            weight = 1
        if node1 not in self.graph:
            self.add_node(node1)
        if node2 not in self.graph:
            self.add_node(node2)

        self.graph[node1][node2] = weight
        if not self.directed:
            self.graph[node2][node1] = weight

    def remove_node(self):
        pass

    def remove_edge(self):
        pass

    def get_neighbors(self):
        pass

    def display_graph(self):
        for node in self.graph:
            print(f'{node}: {self.graph[node]}')


if __name__ == '__main__':
    graph = Graph(directed=False, weighted=False)
    graph.add_node('A')
    graph.add_edge('A', 'B')
    graph.add_edge('B', 'C')
    graph.display_graph()

    graph2 = Graph(directed=False, weighted=True)
    graph2.add_edge("A", "B", 3)
    graph2.add_edge("A", "C", 5)
    graph2.display_graph()
