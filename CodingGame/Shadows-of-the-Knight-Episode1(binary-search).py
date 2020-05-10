import sys
import math

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x, y = [int(i) for i in input().split()] #현재 위치
#x = input()

left_x = 0
right_x = w -1
low_y = 0
high_y = h-1
print(x , file=sys.stderr)
# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    if 'U' in bomb_dir:
        high_y = y-1
    elif 'D' in bomb_dir:
        low_y = y + 1
    else:
        low_y = high_y = y

    if 'R' in bomb_dir:
        left_x = x + 1
    elif 'L' in bomb_dir:
        right_x = x-1
    else:
        left_x = right_x =x

    x = (left_x + right_x) //2
    y = (low_y + high_y) //2

    print(x, y)