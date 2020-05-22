#풀이 1 - 통과
def solution(n, edge):
    children_list = [[] for _ in range(n + 1)]
    distance_list = [0 for _ in range(n + 1)]
    visited_list = [False for _ in range(n + 1)]
    for i in edge:
        stop1 = i[0]
        stop2 = i[1]
        children_list[stop1].append(stop2)
        children_list[stop2].append(stop1)

    open_list = [1]
    closed_list = []

    while open_list:
        current_key=open_list.pop(0)
        visited_list[current_key] = True
        closed_list.append(current_key)

        for children_key in children_list[current_key]:
            if not visited_list[children_key]:
                distance_list[children_key] = distance_list[current_key] + 1
                open_list.append(children_key)
                visited_list[children_key] = True

    return distance_list.count(max(distance_list))


#풀이 2 - test case 8,9 시간 초과
from collections import deque
class Node:
    def __init__(self, number):
        self.number = number
        self.distance = 0
        self.children = deque([])

    def connect(self, other):
        self.children.append(other)

class Graph:
    def __init__(self):
        self.nodes = {}

    def connect(self, id1, id2):
        if id1 not in self.nodes:
            self.nodes[id1] = Node(id1)
        if id2 not in self.nodes:
            self.nodes[id2] = Node(id2)
        self.nodes[id1].connect(self.nodes[id2])
        self.nodes[id2].connect(self.nodes[id1])

def solution(n, edge):
    answer = 0
    graph = Graph()
    for i in edge:
        stop1 = i[0]
        stop2 = i[1]
        graph.connect(stop1, stop2)

    open_list = deque([graph.nodes[1]])
    closed_list = deque([])
    max_distance =0
    count = 0
    while open_list:
        current = open_list.popleft()
        closed_list.append(current)

        for node in current.children:
            if node not in closed_list and node not in open_list:
                node.distance = current.distance + 1
                if node.distance > max_distance:
                    max_distance = node.distance
                    count =1
                elif node.distance == max_distance:
                    count += 1
                open_list.append(node)

    #distance_list = [value.distance for value in nodes.values()]
    #max_distance = max(distance_list)

    #answer = distance_list.count(max_distance)

    return count