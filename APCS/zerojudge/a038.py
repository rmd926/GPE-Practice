# https://zerojudge.tw/ShowProblem?problemid=a038

n = int(input())
rev_num = 0
while n > 0:
    d = n % 10
    n //= 10
    rev_num = rev_num * 10 + d

print(rev_num)