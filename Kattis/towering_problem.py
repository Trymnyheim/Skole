# https://open.kattis.com/problems/towering

from sys import stdin

input = [int(x) for x in next(stdin).split(" ")]

values = input[:6]
height = input[6:]

for i in range(len(values)):
    for j in range(len(values)):
        for k in range(len(values)):
            if i == j or j == k or i == k:
                pass
            else:
                num = values[i] + values[j] + values[k]
                if num == height[0]:
                    tower_1 = [values[i], values[j], values[k]]
                    break
tower_2 = []
for n in values:
    if n not in tower_1:
        tower_2.append(n)
for n in reversed(sorted(tower_1)):
    print(n, end=" ")
for n in reversed(sorted(tower_2)):
    print(n, end=" ")


    
