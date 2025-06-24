# https://zerojudge.tw/ShowProblem?problemid=f605

n, d = map(int, input().split())
item = 0
cost = 0
for i in range(n):
    a, b, c = map(int, input().split())

    if max(a,b,c) - min(a,b,c) >= d:
        item += 1
        cost += (a+b+c) // 3

print(item, cost)
