#! /usr/bin/env python3.4

import time
import random
from collections import deque

__author__ = 'Rodion "rodde" Efremov'


class DirectedGraphNode:
    def __init__(self, name):
        if name is None:
            raise ValueError("The name of a new node is None.")
        self.name = name
        self.children = set()
        self.parents = set()

    def __hash__(self):
        return self.name.__hash__()

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        return "[DirectedGraphNode: " + self.name + "]"

    def add_child(self, child):
        self.children.add(child)
        child.parents.add(self)

    def has_child(self, child_candidate):
        return child_candidate in self.children

    def get_children(self):
        return self.children

    def get_parents(self):
        return self.parents


def traceback_path(target, parents):
    path = []
    current = target

    while current:
        path.append(current)
        current = parents[current]

    return list(reversed(path))


def bi_traceback_path(touch_node, parents_a, parents_b):
    path = []
    current = touch_node

    while current:
        path.append(current)
        current = parents_a[current]

    path = list(reversed(path))
    current = parents_b[touch_node]

    while current:
        path.append(current)
        current = parents_b[current]

    return path


def breadth_first_search(source, target):
    queue = deque([source])
    parents = {source: None}

    while len(queue) > 0:
        current = queue.popleft()

        if current is target:
            return traceback_path(target, parents)

        for child in current.get_children():
            if child not in parents.keys():
                parents[child] = current
                queue.append(child)

    return []


def bidirectional_breadth_first_search(source, target):
    queue_a = deque([source])
    queue_b = deque([target])
    parents_a = {source: None}
    parents_b = {target: None}
    distance_a = {source: 0}
    distance_b = {target: 0}

    # best_cost is ugly
    best_cost = 1000000000
    touch_node = None

    while len(queue_a) > 0 and len(queue_b) > 0:
        dist_a = distance_a[queue_a[0]]
        dist_b = distance_b[queue_b[0]]

        if touch_node and best_cost < dist_a + dist_b:
            return bi_traceback_path(touch_node,
                                     parents_a,
                                     parents_b)
        # Trivial load balancing
        if dist_a < dist_b:
            current = queue_a.popleft()

            if current in distance_b.keys() and best_cost > dist_a + dist_b:
                best_cost = dist_a + dist_b
                touch_node = current

            for child in current.get_children():
                if child not in distance_a.keys():
                    distance_a[child] = distance_a[current] + 1
                    parents_a[child] = current
                    queue_a.append(child)
        else:
            current = queue_b.popleft()

            if current in distance_a.keys() and best_cost > dist_a + dist_b:
                best_cost = dist_a + dist_b
                touch_node = current

            for parent in current.get_parents():
                if parent not in distance_b.keys():
                    distance_b[parent] = distance_b[current] + 1
                    parents_b[parent] = current
                    queue_b.append(parent)
    return []

def create_directed_graph(nodes, edges):
    graph = []

    for i in range(0, nodes):
        node = DirectedGraphNode("" + str(i))
        graph.append(node)

    for i in range(0, edges):
        j = random.randint(0, nodes - 1)
        k = random.randint(0, nodes - 1)
        graph[j].add_child(graph[k])

    return graph


def main():
    graph = create_directed_graph(300000, 1000000)
    source = random.choice(graph)
    target = random.choice(graph)

    print("Source: ", source)
    print("Target: ", target)

    start_time = time.time()
    path1 = breadth_first_search(source, target)
    end_time = time.time()

    print("BFS path length", len(path1), ":")

    for node in path1:
        print(node)

    print("Time elapsed:", 1000.0 * (end_time - start_time), "milliseconds.")
    print()

    start_time = time.time()
    path2 = bidirectional_breadth_first_search(source, target)
    end_time = time.time()

    print("BiBFS path length", len(path2), ":")

    for node in path2:
        print(node)

    print("Time elapsed:", 1000.0 * (end_time - start_time), "milliseconds.")

if __name__ == "__main__":
    main()

