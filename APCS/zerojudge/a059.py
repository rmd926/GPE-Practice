# https://zerojudge.tw/ShowProblem?problemid=a059

TC = int(input())
for i in range(TC):
    n1 = int(input())
    n2 = int(input())
    ans = 0
    
    for num in range(n1, n2+1):
        root = int(num ** 0.5)
        if num == root ** 2: # n must be perfect square num in this case. 
            ans += num
    print(f"Case {i+1}: {ans}")