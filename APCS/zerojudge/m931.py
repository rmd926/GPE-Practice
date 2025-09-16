# https://zerojudge.tw/ShowProblem?problemid=m931
n = int(input())
pairs = []
temp = []

for _ in range(n):
    a, d = map(int, input().split())
    pairs.append((a,d))

temp = [a*a + d*d for a, d in pairs]
target = sorted(temp)[-2]

for a,d in pairs:
    if a**2 + d**2 == target:
        print(a, d)
        break
