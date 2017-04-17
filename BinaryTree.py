# Defines a binary tree
class BinaryTree():
	
	def __init__(self):
		self.left = None
		self.right = None
		self.data = None

	def set_left(self, tree):
		if isinstance(tree, BinaryTree): 
			self.left = tree

	def get_left(self):
		return self.left

	def set_right(self, tree):
		if isinstance(tree, BinaryTree):
			self.right = tree

	def get_right(self):
		return self.right

	def set_data(self, data):
		self.data = data

	def get_data(self):
		return self.data

	def bfs(self):
		bfs_output = list()
		current_node = self
		bfs_output.append(self)
		current_index = 0
		while current_index < len(bfs_output):
			current_node = bfs_output[current_index]
			left_subtree = current_node.get_left()
			if left_subtree:
				bfs_output.append(left_subtree)
			right_subtree = current_node.get_right()
			if right_subtree:
				bfs_output.append(right_subtree)
			current_index += 1
		return bfs_output

	def dfs(self):
		dfs_output = list()
		dfs_output.append(self)
		left_subtree = self.get_left()
		if left_subtree:
			dfs_output.extend(left_subtree.dfs())
		right_subtree = self.get_right()
		if right_subtree:
			dfs_output.extend(right_subtree.dfs())
		return dfs_output

	def full_nodes(self):
		full_node_list = list()
		bfs_traversal_list = self.bfs()
		for node in bfs_traversal_list:
			if node.get_left() and node.get_right():
				full_node_list.append(node)
		return full_node_list

	def deepest_node(self):
		return self.bfs()[-1]

	def print_list(self, function):
		list_to_print = list()
		if function == 'bfs':
			list_to_print = self.bfs()
		if function == 'dfs':
			list_to_print = self.dfs()	
		if function == 'full_nodes':
			list_to_print = self.full_nodes()
		for node in list_to_print:
			print (node.get_data())
		print ("\n")
