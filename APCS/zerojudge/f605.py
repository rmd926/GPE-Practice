# https://zerojudge.tw/ShowProblem?problemid=f605
'''
method 1:
n, d = map(int, input().split())
item = 0
cost = 0
for i in range(n):
    a, b, c = map(int, input().split())

    if max(a,b,c) - min(a,b,c) >= d:
        item += 1
        cost += (a+b+c) // 3

print(item, cost)
'''

'''
method 2:
'''
n, d = map(int, input().split())

item = 0   
cost = 0   
for _ in range(n):
    # 一次讀三天價格到 list 裡
    target = [int(i) for i in input().split()]

    # 如果三天最高價與最低價之差 ≥ d，就要買
    if max(target) - min(target) >= d:
        item += 1
        cost += sum(target) // 3

print(item, cost)
