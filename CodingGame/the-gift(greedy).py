import sys
import math

def get_total_budget(budgets):
    total=0
    for i in budgets:
        total += i
    return total

n = int(input())
cost = int(input())
budgets = [int(input()) for i in range(n)]
budgets = sorted(budgets)
remaining = n
total_budget=get_total_budget(budgets)
spent = []

if total_budget < cost:
    print("IMPOSSIBLE")
else:
    for i in range(n):
        budget = budgets[i]
        avg = cost // remaining

        if budget < avg:
            spent.append(budget)
            cost -= budget
        else:
            spent.append(avg)
            cost -= avg

        remaining -= 1

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr)

for i in spent:
    print(i)