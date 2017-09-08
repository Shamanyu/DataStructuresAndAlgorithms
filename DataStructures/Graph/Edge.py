from Node import Node

class Edge(object):

  def __init__(self):
    self.set_input(None, None)

  def set_input(self, source_node, destination_node):
    self.set_source_node(source_node)
    self.set_destination_node(destination_node)

  def set_source_node(self, source_node):
    self.source_node = source_node

  def set_destination_node(self, destination_node):
    self.destination_node = destination_node

  def get_source_node(self):
    return self.source_node

  def get_destination_node(self):
    return self.destination_node

  def print_edge(self):
    self.get_source_node().print_node()
    self.get_destination_node().print_node()
    print ('')
