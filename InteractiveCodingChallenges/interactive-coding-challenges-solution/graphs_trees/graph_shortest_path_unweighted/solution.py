from collections import deque

from graph import State, Node, Graph


class GraphShortestPath(Graph):

    # Time complexity: O(V+E); where 'V' is the number of vertices and 'E' is the number of edges
    # Space complexity: O(V+E); where 'V' is the number of vertices and 'E' is the number of edges
    def shortest_path(self, source_key, dest_key):
        if source_key is None or dest_key is None:
            return None
        if source_key is dest_key:
            return [source_key]
        prev_node_keys = self._shortest_path(source_key, dest_key)
        if prev_node_keys is None:
            return None
        else:
            path_ids = [dest_key]
            prev_node_key = prev_node_keys[dest_key]
            while prev_node_key is not None:
                path_ids.append(prev_node_key)
                prev_node_key = prev_node_keys[prev_node_key]
            return path_ids[::-1]

    def _shortest_path(self, source_key, dest_key):
        queue = deque()
        queue.append(self.nodes[source_key])
        prev_node_keys = {source_key: None}
        self.nodes[source_key].visit_state = State.unvisited
        while queue:
            node = queue.popleft()
            if node.key is dest_key:
                return prev_node_keys
            prev_node = node
            for adj_node in node.adj_nodes.values():
                if adj_node.visit_state == State.unvisited:
                    queue.append(adj_node)
                    prev_node_keys[adj_node.key] = prev_node.key
                    adj_node.visit_state = State.visited
        return None


# %load test_shortest_path.py
from nose.tools import assert_equal

class TestShortestPath(object):

    def test_shortest_path(self):
        nodes = []
        graph = GraphShortestPath()
        for id in range(0, 6):
            nodes.append(graph.add_node(id))
        graph.add_edge(0, 1)
        graph.add_edge(0, 4)
        graph.add_edge(0, 5)
        graph.add_edge(1, 3)
        graph.add_edge(1, 4)
        graph.add_edge(2, 1)
        graph.add_edge(3, 2)
        graph.add_edge(3, 4)

        assert_equal(graph.shortest_path(nodes[0].key, nodes[2].key), [0, 1, 3, 2])
        assert_equal(graph.shortest_path(nodes[0].key, nodes[0].key), [0])
        assert_equal(graph.shortest_path(nodes[4].key, nodes[5].key), None)

        print('Success: test_shortest_path')


def main():
    test = TestShortestPath()
    test.test_shortest_path()


if __name__ == '__main__':
    main()