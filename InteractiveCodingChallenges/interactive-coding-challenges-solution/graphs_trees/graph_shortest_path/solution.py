import sys

from priority_queue import PriorityQueueNode, PriorityQueue
from graph import State, Node, Graph

class ShortestPath(object):

    def __init__(self, graph):
        if graph is None:
            raise TypeError('Graph cannot be none')
        self.graph = graph
        self.previous = {}
        self.path_weight = {}
        self.remaining = PriorityQueue()
        for key in self.graph.nodes.keys():
            self.previous[key] = None
            self.path_weight[key] = sys.maxsize
            self.remaining.insert(
              PriorityQueueNode(key, self.path_weight[key]))

    # Time complexity(Array based priority queue): O(V^2); where 'V' is the number of vertices
    # Time complexity(Min heap based priority queue): O((V+E)logV); where 'V' is the number of vertices and 'E' is the number of edges
    # Space complexity(Array based priority queue): O(V^2); where 'V' is the number of vertices
    # Space complexity(Array based priority queue): O((V+E)logV); where 'V' is the number of vertices and 'E' is the number of edges
    def find_shortest_path(self, start_node_key, end_node_key):
        if start_node_key is None or end_node_key is None:
            raise TypeError('Input node keys cannot be none')
        if (start_node_key not in self.graph.nodes or
          end_node_key not in self.graph.nodes):
            raise ValueError('Invalid start or end node key')
        self.path_weight[start_node_key] = 0
        self.remaining.decrease_key(start_node_key, 0)
        while self.remaining:
            min_node_key = self.remaining.extract_min().obj
            min_node = self.graph.nodes[min_node_key]
            for adj_key in min_node.adj_nodes.keys():
                new_weight = (min_node.adj_weights[adj_key] +
                  self.path_weight[min_node_key])
                if self.path_weight[adj_key] > new_weight:
                    self.previous[adj_key] = min_node_key
                    self.path_weight[adj_key] = new_weight
                    self.remaining.decrease_key(adj_key, new_weight)
        result = list()
        current_node_key = end_node_key
        while current_node_key is not None:
            result.append(current_node_key)
            current_node_key = self.previous[current_node_key]
        return result[::-1]


# %load test_shortest_path.py
from nose.tools import assert_equal

class TestShortestPath(object):

    def test_shortest_path(self):
        graph = Graph()
        graph.add_edge('a', 'b', weight=5)
        graph.add_edge('a', 'c', weight=3)
        graph.add_edge('a', 'e', weight=2)
        graph.add_edge('b', 'd', weight=2)
        graph.add_edge('c', 'b', weight=1)
        graph.add_edge('c', 'd', weight=1)
        graph.add_edge('d', 'a', weight=1)
        graph.add_edge('d', 'g', weight=2)
        graph.add_edge('d', 'h', weight=1)
        graph.add_edge('e', 'a', weight=1)
        graph.add_edge('e', 'h', weight=4)
        graph.add_edge('e', 'i', weight=7)
        graph.add_edge('f', 'b', weight=3)
        graph.add_edge('f', 'g', weight=1)
        graph.add_edge('g', 'c', weight=3)
        graph.add_edge('g', 'i', weight=2)
        graph.add_edge('h', 'c', weight=2)
        graph.add_edge('h', 'f', weight=2)
        graph.add_edge('h', 'g', weight=2)
        shortest_path = ShortestPath(graph)
        result = shortest_path.find_shortest_path('a', 'i')
        assert_equal(result, ['a', 'c', 'd', 'g', 'i'])
        assert_equal(shortest_path.path_weight['i'], 8)

        print('Success: test_shortest_path')


def main():
    test = TestShortestPath()
    test.test_shortest_path()


if __name__ == '__main__':
    main()