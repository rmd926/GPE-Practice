T = int(input())
for i in range(T):
    L, W, H = map(int, input().split())
    limit = 20
    if L <= limit and W <= limit and H <= limit:
        print(f"Case {i+1}: good")
    else:
        print(f"Case {i+1}: bad")