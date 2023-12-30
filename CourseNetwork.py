from Graph import Graph
from CourseTitle import CourseTitle
from pyvis.network import Network


class CourseNetwork:
    """ This class implements the graph data structure defined in Graph.py to build a network of courses.

    This class acts as a graph builder so that the creation of the graph is handled outside of Main.py.
    The weights of the graph are NOT costs - instead, they act as tags to allow for optional edges. This allowed for the
    representation of 'required' edges and 'optional' edges.

    Attributes:
        graph (Graph): A network of courses: graph containing CourseTitle objects as vertices and their prerequisites as
                       edges


    """
    def __init__(self):
        self.graph = Graph()
        self.net = Network(notebook=True, cdn_resources="remote", height="750px", width="100%", bgcolor="#222222", font_color="white")

    def build_graph(self, courses):
        for course in courses:
            vertex = course.get_info()
            self.net.add_node(str(vertex))
            prerequisites = course.get_prerequisites().get_stream()
            for prereq in prerequisites:
                if isinstance(prereq, CourseTitle) or prereq == 'None':
                    self.graph.add_edge(vertex, prereq, 0)
                    if prereq != 'None':
                        try:
                            self.net.add_edge(str(vertex), str(prereq))
                        except AssertionError:
                            self.net.add_node(str(prereq))
                            self.net.add_edge(str(vertex), str(prereq))

        return self.graph

    def display_network(self):
        self.net.toggle_physics(True)
        self.net.show('course_network.html')
