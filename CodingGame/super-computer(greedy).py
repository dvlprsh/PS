import sys
import math
'''
ending_list = [[start_day, ending_day]]
ending_list.sort(by ending_day)
for i range(n):
    if 마지막 ending_day > 현재 start_day:
        schedule_list.append(현재 ending_day)
'''
schedule_list = []
ending_list = []
n = int(input())
for i in range(n):
    start_day, duration = [int(j) for j in input().split()]
    end_day = start_day + duration -1
    ending_list.append([start_day, end_day])

ending_list=sorted(ending_list, key=lambda ending_list: ending_list[1])

for i in range(n):
    if i == 0:
        schedule_list.append(ending_list[i][1])
    else:
        if schedule_list[-1] < ending_list[i][0]:
            schedule_list.append(ending_list[i][1])

print(len(schedule_list))