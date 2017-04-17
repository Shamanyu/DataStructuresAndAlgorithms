from BinaryTree import BinaryTree

root = BinaryTree()
root.set_data(1)

node_11 = BinaryTree()
node_11.set_data(2)
root.set_left(node_11)

node_12 = BinaryTree()
node_12.set_data(3)
root.set_right(node_12)

node_21 = BinaryTree()
node_21.set_data(4)
node_11.set_left(node_21)

node_22 = BinaryTree()
node_22.set_data(5)
node_11.set_right(node_22)

node_23 = BinaryTree()
node_23.set_data(6)
node_12.set_left(node_23)

node_24 = BinaryTree()
node_24.set_data(7)
node_12.set_right(node_24)

node_31 = BinaryTree()
node_31.set_data(8)
node_21.set_left(node_31)

node_32 = BinaryTree()
node_32.set_data(9)
node_21.set_right(node_32)

node_35 = BinaryTree()
node_35.set_data(12)
node_23.set_left(node_35)

node_38 = BinaryTree()
node_38.set_data(15)
node_24.set_right(node_38)

node_41 = BinaryTree()
node_41.set_data(16)
node_31.set_left(node_41)

node_42 = BinaryTree()
node_42.set_data(17)
node_38.set_left(node_42)

node_43 = BinaryTree()
node_43.set_data(18)
node_38.set_right(node_43)

node_50 = BinaryTree()
node_50.set_data(19)
node_41.set_right(node_50)

node_60 = BinaryTree()
node_60.set_data(20)
node_50.set_left(node_60)

node_70 = BinaryTree()
node_70.set_data(21)
node_60.set_left(node_70)

root.print_list('bfs')
root.print_list('dfs')
root.print_list('full_nodes')
print (root.deepest_node().get_data())
