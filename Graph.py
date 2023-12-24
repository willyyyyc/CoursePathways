from collections import defaultdict
class Graph:
    def __init__(self, num_of_nodes=0):
        self.num_of_nodes = num_of_nodes
        self.adjacency_list = defaultdict(list)

    def add_edge(self, vertex, edges):
        self.adjacency_list[vertex].append(edges)
        self.num_of_nodes += 1

    def get_size(self):
        return self.num_of_nodes

    def __str__(self):
        for vertex in self.adjacency_list.keys():
            print("course: " + vertex + " prerequisites: " + str(self.adjacency_list[vertex]))