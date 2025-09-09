# https://zerojudge.tw/ShowProblem?problemid=g595
# method 1: Dealing with border issues
n = int(input())
h = [int(x) for x in input().split()]

total = 0
if h[0] == 0:
    total += h[1]

if h[n-1] == 0:
    total += h[n-2]

for i in range(1, len(h)-1):
    if h[i] == 0:
        total += min(h[i-1], h[i+1])
print(total)

# method 2: Put some big nums on left and right sides.

n = int(input())
h = [int(x) for x in input().split()]

total = 0
# if h[0] == 0:
#     total += h[1]

# if h[n-1] == 0:
#     total += h[n-2]
INF = 100000000
h = [INF]+h+[INF]
for i in range(len(h)):
    if h[i] == 0:
        total += min(h[i-1], h[i+1])
print(total)

