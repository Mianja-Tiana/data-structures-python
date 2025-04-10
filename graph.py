class NodeGraph:
    def __init__(self, data):
        self.data = data
        self.neighbors = []

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, data):
        if data not in self.nodes:
            self.nodes[data] = NodeGraph(data)

    def add_edge(self, data1, data2):
        self.add_node(data1)
        self.add_node(data2)
        self.nodes[data1].neighbors.append(self.nodes[data2])
        self.nodes[data2].neighbors.append(self.nodes[data1])  

    def display(self):
        for node in self.nodes.values():
            print(f"{node.data}: {[neighbor.data for neighbor in node.neighbors]}")
my_graph = Graph()
my_graph.add_node("A")
my_graph.add_node("B")
my_graph.add_edge("A", "B")
my_graph.add_edge("B", "C")
my_graph.display()