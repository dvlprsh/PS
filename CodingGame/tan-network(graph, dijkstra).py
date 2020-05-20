import sys
import math
class Node:
    def __init__(self, identifier, name, latitude, longitude):
        self.identifier = identifier
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.distance = 0.0
        self.parent = None
        self.children = []

    def get_distance(self, other):
        x = math.radians(other.longitude - self.longitude) * math.cos(math.radians((self.latitude + other.latitude) / 2.0))
        y = math.radians(other.latitude - self.latitude)
        return math.sqrt(x * x + y * y) * 6371.0

    def connect(self, other):
        self.children.append(other)

class Graph:
    def __init__(self):
        self.nodes = {}

    def insert(self, uid, node):
        self.nodes[uid] = node

    def connect(self, id1, id2):
        self.nodes[id1].connect(self.nodes[id2])

    def find_shortest_path(self, start_id, end_id):
        start_stop = self.nodes[start_id]
        end_stop = self.nodes[end_id]
        open_list = [start_stop]
        closed_list = []

        while open_list:
            current = open_list.pop(0)
            closed_list.append(current)
            if current.identifier == end_stop.identifier:
                #도착 정저강을 찾으면 최단 경로를 지나는 정거장 이름을 배열에 담아 반환
                path = []
                while current is not None:
                    #경로 출력 시 정거장 이름이 필요
                    path.append(current.name)
                    current = current.parent
                return path[::-1]

            for neighbor in current.children:
                if neighbor in open_list:
                    #이미 열린 목록에 있는 경우 두 경로의 거리를 비교한다
                    exist_one = open_list[open_list.index(neighbor)]
                    new_distance = current.distance + neighbor.get_distance(current)
                    if new_distance < exist_one.distance:
                        exist_one.parent = current
                        exist_one.distance = new_distance

                elif neighbor not in closed_list and neighbor not in open_list:
                    #열린 목록과 닫힌 목록에 모두 없으면 탐색하지 않은 노드잉므로 열린 목록에 추가
                    neighbor.parent = current
                    neighbor.distance = current.distance + neighbor.get_distance(current)
                    open_list.append(neighbor)
            #열린 목록을 거리순으로 정렬
            open_list = sorted(open_list, key=lambda x: x.distance)
        return []

start_id = input().split(':')[1]
end_id = input().split(':')[1]

tan = Graph()

n = int(input())
for i in range(n):
    stop_info = input().split(',')
    identifier = stop_info[0].split(':')[1]
    name = stop_info[1].strip('\"')
    latitude = float(stop_info[3])
    longitude = float(stop_info[4])
    tan.insert(identifier, Node(identifier, name, latitude, longitude))

m = int(input())
for i in range(m):
    stop_area1, stop_area2 = input().split(' ')
    stop1_id = stop_area1.split(':')[1]
    stop2_id = stop_area2.split(':')[1]
    tan.connect(stop1_id, stop2_id)

path=tan.find_shortest_path(start_id, end_id)
# To debug: print("Debug messages...", file=sys.stderr)

if len(path) > 0:
    for stop in path:
        print(stop)
else:
    print('IMPOSSIBLE')