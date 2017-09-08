from Node import Node
from Edge import Edge

class Graph(object):

  def __init__(self):
    self.set_nodes(list())
    self.set_edges(list())

  def set_nodes(self, nodes):
    self.nodes = nodes

  def add_node(self, node):
    self.nodes.append(node)

  def remove_node(self, node):
    edges_to_remove = list()
    for edge in self.edges[:]:
      if node == edge.get_source_node() or node == edge.get_destination_node():
        self.remove_edge(edge)
    try:
      self.nodes.remove(node)
    except:
      pass

  def set_edges(self, edges):
    self.edges = list()
    for edge in edges:
      self.add_edge(edge)

  def add_edge(self, edge):
    if edge.get_source_node() in self.nodes and edge.get_destination_node() in self.nodes:
      self.edges.append(edge)

  def remove_edge(self, edge):
    try:
      self.edges.remove(edge)
    except:
      pass

  def get_nodes(self):
    return self.nodes

  def get_edges(self):
    return self.edges

  def print_nodes(self):
    print ("Nodes are:")
    for node in self.get_nodes():
      node.print_node()

  def print_edges(self):
    print ("Edges are:")
    for edge in self.get_edges():
      edge.print_edge()

  def print_graph(self):
    self.print_nodes()
    print('')
    self.print_edges()

# node1 = Node()
# node1.set_value(1)
# node2 = Node()
# node2.set_value(2)
# node3 = Node()
# node3.set_value(3)
# node4 = Node()
# node4.set_value(4)
# node5 = Node()
# node5.set_value(5)

# edge1 = Edge()
# edge1.set_input(node1, node1)
# edge2 = Edge()
# edge2.set_input(node1, node2)
# edge3 = Edge()
# edge3.set_input(node2, node1)
# edge4 = Edge()
# edge4.set_input(node3, node4)
# edge5 = Edge()
# edge5.set_input(node4, node5) 

# graph = Graph()
# graph.set_nodes([node1, node2, node3, node4])
# graph.set_edges([edge1, edge2, edge3, edge4])

# graph.print_graph()

# graph.add_edge(edge5)
# graph.print_graph()

# graph.remove_node(node2)
# graph.remove_edge(edge4)
# graph.remove_node(None)
# graph.remove_edge(None)
# graph.print_graph()
