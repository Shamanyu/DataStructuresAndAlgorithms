from results import Results
from graph import State, Node, Graph

class GraphBfs(Graph):

    # Time complexity: O(V+E); where 'V' is the number of nodes and 'E' is the number of edges
    # Space complexity: O(V); where 'n' is the number of nodes
    def bfs(self, root, visit_func):
        if root is None:
            return
        queue = [root]
        while len(queue) > 0:
            node = queue.pop(0)
            if node.visit_state == State.unvisited:
                visit_func(node)
                node.visit_state = State.visited
                for neighbour in node.adj_nodes.values():
                    queue.append(neighbour) 


# %load test_bfs.py
from nose.tools import assert_equal

class TestBfs(object):

    def __init__(self):
        self.results = Results()

    def test_bfs(self):
        nodes = []
        graph = GraphBfs()
        for id in range(0, 6):
            nodes.append(graph.add_node(id))
        graph.add_edge(0, 1, 5)
        graph.add_edge(0, 4, 3)
        graph.add_edge(0, 5, 2)
        graph.add_edge(1, 3, 5)
        graph.add_edge(1, 4, 4)
        graph.add_edge(2, 1, 6)
        graph.add_edge(3, 2, 7)
        graph.add_edge(3, 4, 8)
        graph.bfs(nodes[0], self.results.add_result)
        assert_equal(str(self.results), "[0, 1, 4, 5, 3, 2]")

        print('Success: test_bfs')


def main():
    test = TestBfs()
    test.test_bfs()


if __name__ == '__main__':
    main()