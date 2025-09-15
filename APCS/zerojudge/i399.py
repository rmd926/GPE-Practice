# https://zerojudge.tw/ShowProblem?problemid=i399
from collections import Counter
target = [int(x) for x in input().split()]
print(Counter(target).most_common()[0][1], *sorted(set(target))[::-1])
