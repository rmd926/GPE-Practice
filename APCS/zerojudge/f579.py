# https://zerojudge.tw/ShowProblem?problemid=f579

a, b = map(int,input().split())
n = int(input())
ans = 0
for i in range(n):
    count_a = 0
    count_b = 0
    record = [int(i) for i in input().split()]
    for k in record:
        if k == a:
            count_a += 1
        if k == -a:
            count_a -= 1
        if k == b:
            count_b += 1
        if k == -b:
            count_b -= 1

    if count_a > 0 and count_b > 0:
        ans += 1
print(ans)