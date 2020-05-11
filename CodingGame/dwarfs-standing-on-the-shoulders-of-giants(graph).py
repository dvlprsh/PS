import sys
import math
class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
    def __repr__(self):
        return 'Node(' + str(self.value) + ')'

    def __str__(self):
        return 'Node({0}) -> {1}'.format(self.value, self.children)

    def get_height(self):
        max_height = 0
        for child in self.children:
            max_height = max(max_height, child.get_height())
        return max_height + 1

class Graph:
    def __init__(self):
        #전체 노드를 저장하는 변수. key=노드번호
        self.nodes = {}

    def influence(self, x, y): #입력받은 두 노드 번호를 연결
        if x not in self.nodes:
            self.nodes[x] = Node(x)
        if y not in self.nodes:
            self.nodes[y] = Node(y)
        self.nodes[x].children.append(self.nodes[y])

    def get_graph_height(self):
        graph_height = 0
        for key in self.nodes:
            child_height = self.nodes[key].get_height()
            graph_height = max(graph_height, child_height)
        return graph_height

graph = Graph()

n = int(input())  # the number of relationships of influence
for i in range(n):
    # x: a relationship of influence between two people (x influences y)
    x, y = [int(j) for j in input().split()]
    graph.influence(x, y)

print(graph.get_graph_height())


# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr)


# The number of people involved in the longest succession of influences