class Node():

	def __init__(self, barcode, coordinate, neighbours, size_info, store_status, zone='defzone', blocked='false', botid='null', adjacency=None, special=None):
		self.barcode = barcode
		self.coordinate = coordinate
		self.neighbours = neighbours
		self.size_info = size_info
		self.store_status = store_status
		self.zone = zone
		self.blocked = blocked
		self.botid = botid
		self.adjacency = adjacency
		self.special = special
		[self.row, self.column] = self.decode_barcode(barcode)
		self.set_id(barcode)

	def set_id(self, barcode):
		self.id = self.barcode

	def get_id(self):
		return self.id

	def get_neighbours(self):
		[self.get_neighbour(0), self.get_neighbour(1), self.get_neighbour(2), self.get_neighbour(3)]

	def get_neighbour(self, index):
		if self.adjacency and self.adjacency[index]:
			return self.coordinate_to_barcode(self.adjacency[index])
		elif self.adjacency and not self.adjacency[index]:
			return None
		else:
			return encode_barcode(self.row-1, self.column)

	def encode_barcode(self, row, column):
		return encode_number(row) + '.' + encode_number(column)

	def encode_number(self, number):
		if number < 10:
			return '00' + str(number)
		elif number < 100:
			return '0' + str(number)
		else:
			return str(number)

	def decode_barcode(self, barcode):
		[int(position) for position in barcode.split('.')]

class Map():

	def __init__(self):
		self.nodes = dict()

	def add_node(self, node):
		if isinstance(node, Node):
			self.nodes[node.get_id()] = node

	def read_json(self, map_json):
		for raw_node_data in map_json:
			if 'adjacency' in raw_node_data and 'special' in raw_node_data:
				node =  Node(raw_node_data.barcode, raw_node_data.coordinate, raw_node_data.neighbours, raw_node_data.size_info, raw_node_data.store_status, zone=raw_node_data.store_status, blocked=raw_node_data.blocked, botid=raw_node_data.botid, adjacency=raw_node_data.adjacency, special=raw_node_data.special)
			else:
				node =  Node(raw_node_data.barcode, raw_node_data.coordinate, raw_node_data.neighbours, raw_node_data.size_info, raw_node_data.store_status, zone=raw_node_data.store_status, blocked=raw_node_data.blocked, botid=raw_node_data.botid)
			self.add_node(node)

	def convert_to_json(self, map_json):
		json_data = list()
		for node_id in self.nodes:
			node_data = dict()
			node_data['barcode'] = self.nodes[node_id].barcode
			node_data['coordinate'] = self.nodes[node_id].coordinate
			node_data['neighbours'] = self.nodes[node_id].neighbours
			node_data['size_info'] = self.nodes[node_id].size_info
			node_data['store_status'] = self.nodes[node_id].store_status
			node_data['blocked'] = self.nodes[node_id].blocked
			node_data['botid'] = self.nodes[node_id].botid
			node_data['adjacency'] = self.nodes[node_id].adjacency
			node_data['special'] = self.nodes[node_id].special