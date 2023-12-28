from collections import defaultdict


class Graph:
    """This class represents a graph datastructure.

    Attributes:
        num_of_nodes (int): Number of nodes in the graph

    Methods:
        add_edge(self, vertex, edges): Add an edge to graph
        get_size(self): return number of vertices in graph
        print_graph(self)
    """
    def __init__(self, num_of_nodes=0):
        """Initialize graph with default number of nodes set to 0.

        Uses a default dictionary to represent the adjacency list

        Args:
            num_of_nodes (int): Number of nodes in the graph, defaults to 0

        Returns:
            Graph object
        """
        self.num_of_nodes = num_of_nodes
        self.adjacency_list = defaultdict(list)

    def add_edge(self, vertex, edges):
        """Add an edge to graph.

        Increases number of nodes in the graph by 1

        Args:
            vertex (Course): New addition to graph
            edges (list): List of vertices to which the new vertex is connected

        Returns:
            void
        """
        self.adjacency_list[vertex].append(edges)
        self.num_of_nodes += 1

    def get_size(self):
        """Return the number of vertices in the graph.

        Return:
            num_of_nodes (int): Number of vertices in the graph
        """
        return self.num_of_nodes

    def print_graph(self):
        """Display vertices in Graph.

        Returns:
            String representation of graph
        """
        for vertex in self.adjacency_list.keys():
            print("Course: " + str(vertex) + "\nPrerequisites: " + str(self.adjacency_list[vertex]) + "\n")