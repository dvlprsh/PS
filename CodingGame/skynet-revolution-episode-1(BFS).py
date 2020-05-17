import sys
import math

class Node:
    def __init__(self, number):
        self.number = number
        self.parent = None
        self.children = []

    def connect(self, other):
        self.children.append(other)

class Graph:
    def __init__(self):
        self.nodes = {}

    def connect(self, x, y):
        if x not in self.nodes:
            self.nodes[x] = Node(x)
        if y not in self.nodes:
            self.nodes[y] = Node(y)
        self.nodes[x].connect(self.nodes[y])
        self.nodes[y].connect(self.nodes[x])

    def find_shortest_path(self, start, goal):
        open_list = [self.nodes[start]]
        closed_list = []

        while open_list:
            current = open_list.pop(0)
            closed_list.append(current)
            if current.number == goal:
                shortest_path = []
                while current.number != start:
                    shortest_path.append(current.number)
                    current = current.parent
                shortest_path.append(start)
                return shortest_path[::-1]

            for node in current.children:
                if node in closed_list or node in open_list:
                    continue
                node.parent = current
                open_list.append(node)
        #모든 노드를 탐색하고도 목적지를 찾지 못하면 빈 배열을 반환
        return []

    def remove_connection(self, x, y):
        self.nodes[x].children.remove(self.nodes[y])
        self.nodes[y].children.remove(self.nodes[x])

graph = Graph()
exit = []
# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
n, l, e = [int(i) for i in input().split()]
for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]
    graph.connect(n1, n2)
exits=[int(input()) for i in range(e)]

# game loop
while True:
    si = int(input())  # The index of the node on which the Skynet agent is positioned this turn
    shortest_path = None
    for exit in exits:
        path = graph.find_shortest_path(si, exit)
        if len(path) > 0:
            if shortest_path == None or len(shortest_path) > len(path):
                shortest_path=path

    # Example: 0 1 are the indices of the nodes you wish to sever the link between
    print(shortest_path[-1], shortest_path[-2])
    graph.remove_connection(shortest_path[-1], shortest_path[-2])