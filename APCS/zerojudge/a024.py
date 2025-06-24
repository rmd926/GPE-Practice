# https://zerojudge.tw/ShowProblem?problemid=a024

x, y = map(int, input().split())
while x != 0 and y != 0:
    if x > y:
        x = x % y
    elif y > x:
        y = y % x
    else:
        break

if x == 0:
    print(y)
else:
    print(x)
