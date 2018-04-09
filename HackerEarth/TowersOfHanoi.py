node_radius = dict()
node_height = dict()
node_edges = dict()
T = int(raw_input(''))
for test_case_number in range(T):
	N = int(raw_input(''))
	for node_number in range(N):
		radius, height = raw_input('').split()
		radius = int(radius)
		height = int(height)
		node_radius[node_number] = radius
		node_height[node_number] = height
		node_edges[node_number] = list()
	for node1 in node_edges:
		for node2 in node_edges:
			if node_radius[node1] > node_radius[node2] and node_height[node1] > node_height[node2]:
				node_edges[node2].append(node1)

	print node_edges
