n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    
    print((a//3) * (b//3))
