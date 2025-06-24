# https://zerojudge.tw/ShowProblem?problemid=f312

a1, b1, c1 = map(int,input().split())
a2, b2, c2 = map(int,input().split())

n = int(input())
revenue = - 10000 # 因為有可能是負的，所以設一個負蠻大的值。
for x1 in range(n+1):
    y1 = a1*(x1**2) + b1*x1 + c1
    x2 = n - x1
    y2 = a2*(x2**2) + b2*x2 + c2

    if y1+y2 > revenue: # update
        revenue = y1+y2

print(revenue)
