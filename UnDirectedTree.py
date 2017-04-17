class Node():

	def __init__(self):
		self.data = None

	def set_data(self, data):
		self.data = data

	def get_data(self):
		return self.data

class Edge():

	def __init__(self):
		self.nodes = (None, None)

	def set_edge(self, node1, node2):
		self.nodes = (node1, node2)

	def get_edge(self):
		return self.nodes

class Tree():

	def __init__(self):
		self.nodes = list()
		self.edges = list()

	def add_node(self, node):
		self.nodes.append(node)

	def get_nodes(self):
		return self.nodes

	def add_edge(self, edge):
		self.edges.append(edge)

	def get_edges(self):
		return self.edges


