import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l, c, n = [int(i) for i in input().split()]
groups = [int(input()) for i in range(n)]

total_passengers = sum(groups)
total_revenue= 0

if total_passengers <= l:
    total_revenue = total_passengers * c
else:
    revenue_history = {}
    next_idx = 0

    for i in range(c):
        num_passengers = 0
        if next_idx in revenue_history:
            next_idx, num_passengers = revenue_history[next_idx]
        else:
            begin_idx = next_idx

            while num_passengers + groups[next_idx] <= l:
                num_passengers += groups[next_idx]
                next_idx = (next_idx + 1) % n
            
            revenue_history[begin_idx] = (next_idx, num_passengers)
        total_revenue += num_passengers
print(total_revenue)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr)