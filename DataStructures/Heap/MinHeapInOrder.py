import heapq

def tree_inorder(index):
	if index < len(data):
		left_child_index = index*2+1
		right_child_index = index*2+2
		return tree_inorder(left_child_index) + [data[index]] + tree_inorder(right_child_index)
	return []

data = list(input(''))

heapq.heapify(data)

current_index = 0

print (tree_inorder(0))
