class Vertex(object):

  def __init__(self, name):
    self.set_vertex(name)

  def get_user_input(self):
    name = input()
    self.set_vertex(name)

  def set_vertex(self, name):
    self.name = name

  def get_vertex(self):
    return self.name

  def print_vertex(self):
    print (self.get_vertex())

class Edge(object):

  def __init__(self, source_vertex, destination_vertex):
    self.set_edge(source_vertex, destination_vertex)

  def get_user_input(self):
    [source_vertex, destination_vertex] = [Vertex(vertex_name) for 
      vertex_name in input().split()]
    self.set_edge(source_vertex, destination_vertex)

  def set_edge(self, source_vertex, destination_vertex):
    self.source_vertex = source_vertex
    self.destination_vertex = destination_vertex
    self.edge = (source_vertex, destination_vertex)

  def get_edge(self):
    return self.edge

  def get_source_vertex(self):
    return self.source_vertex

  def get_destination_vertex(self):
    return self.destination_vertex

  def print_edge(self):
    print(self.source_vertex.get_vertex(), self.destination_vertex.get_vertex())

class Graph(object):

  def __init__(self):
    pass

  def get_user_input(self):
    vertices = [Vertex(vertex_name) for vertex_name in input.split()]
    edge_details = [edge_detail for edge in input.split()]
    edges = list()
    for edge_detail in edge_details:
      (source_vertex_name, destination_vertex_name) = edge_detail
      source_vertex = Vertex(source_vertex_name)
      destination_vertex = Vertex(destination_vertex_name)
      edges.append(Edge(source_vertex, destination_vertex))
    self.set_input(vertices, edges)

  def set_input(self, vertices, edges):
    # import pdb; pdb.set_trace()
    self.number_of_vertices = 0
    self.number_of_edges = 0
    self.vertices = list()
    self.edges = list()
    for vertex in vertices:
      self.add_vertex(vertex)
    for edge in edges:
      self.add_edge(edge)

  def add_vertex(self, vertex):
    self.vertices.append(vertex)
    self.number_of_vertices += 1

  def remove_vertex(self, vertex):
    try:
      self.vertices.remove(vertex)
    except ValueError:
      pass
    self.number_of_vertices -= 1

  def add_edge(self, edge):
    source_vertex = edge.get_source_vertex()
    destination_vertex = edge.get_destination_vertex()
    if source_vertex in self.vertices and destination_vertex in self.vertices:
      self.edges.append(edge)
      self.number_of_edges += 1

  def remove_edge(self, edge):
    try:
      self.edges.remove(edge)
    except ValueError:
      pass
    self.number_of_edges -= 1

  def get_graph(self):
    return [self.vertices, self.edges]

  def print_graph(self):
    print ("\nVertices are: ")
    for vertex in self.vertices:
      vertex.print_vertex()
    print ("\nEdges are: ")
    for edge in self.edges:
      edge.print_edge()
    print("")

vertex_a = Vertex('a')
vertex_b = Vertex('b')

edge_1 = Edge(vertex_a, vertex_b)
edge_2 = Edge(vertex_b, vertex_a)
edge_3 = Edge(vertex_a, vertex_a)

graph = Graph()
graph.set_input([vertex_a, vertex_b], [edge_1, edge_2, edge_3])
graph.print_graph()