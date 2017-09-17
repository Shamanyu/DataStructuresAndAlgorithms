class Node(object):
	def __init__(self, data=None, next_node=None):
		self.data=data
		self.next_node=next_node
	def get_data(self):
		return self.data
	def get_next(self):
		return self.next_node
	def set_next(self, new_next):
		self.next_node = new_next

class LinkedList(object):
	def __init__(self, head=None):
		self.head=head
	def insert(self, data):
		new_node=Node(data)
		new_node.set_next(self.head)
		self.head=new_node
	def size(self):
		current=self.head
		count=0
		while current:
			count+=1
			current=current.get_next()
		return count
	def search(self, data):
		current=self.head
		found=False
		while current and found is False:
			if current.get_data() == data:
				found=True
			else:
				current=current.get_next()
		if current is None:
			return ValueError("Data not in list")
		return current
	def delete(self, data):
		current=self.head
		previous=None
		found=False
		while current and found is False:
			if current.get_data()==data:
				found=True
			else:
				previous=current
				current=current.get_next()
		if current is None:
			raise ValueError("Data not in list")
		if previous is None:
			self.head=current.get_next()
		else:
			previous.set_next(current.get_next())
	def print_list(self):
		node=self.head
		while node:
			print(node.get_data())
			node=node.get_next()

L = LinkedList()
number_of_elements =int(raw_input("\nEnter the number of entries: "))
for x in range(0, number_of_elements):
	L.insert(int((raw_input("\nEnter number: "))))
to_delete=int(raw_input("\nWhich number is to be deleted?"))
while 1:
	try:
		L.delete(to_delete)
	except ValueError:
		break
L.print_list()
