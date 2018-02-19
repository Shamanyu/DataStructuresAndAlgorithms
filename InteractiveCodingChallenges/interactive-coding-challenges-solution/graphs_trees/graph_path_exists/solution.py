from graph import State, Node, Graph


class GraphPathExists(Graph):

    # Time complexity: O(V+E); where 'V' is the number of vertices and 'E' is the number of edges
    # Space complexity: O(V)l where 'V' is the number of edges
    def path_exists(self, start, end):
        if None in (start, end):
            return False
        nodes_to_traverse = [start]
        while len(nodes_to_traverse) > 0:
            node = nodes_to_traverse.pop(0)
            if node.visit_state == State.unvisited:
                node.visit_state == State.visited
                if node == end:
                    return True
                for neighbour in node.adj_nodes.values():
                    nodes_to_traverse.append(neighbour)
        return False



# %load test_path_exists.py
from nose.tools import assert_equal

class TestPathExists(object):

    def test_path_exists(self):
        nodes = []
        graph = GraphPathExists()
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

        assert_equal(graph.path_exists(nodes[0], nodes[2]), True)
        assert_equal(graph.path_exists(nodes[0], nodes[0]), True)
        assert_equal(graph.path_exists(nodes[4], nodes[5]), False)

        print('Success: test_path_exists')


def main():
    test = TestPathExists()
    test.test_path_exists()


if __name__ == '__main__':
    main()