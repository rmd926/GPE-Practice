tc = 1
while True:
    try:
        N, Q = map(int, input().split())
    except:
        break
    if N == Q == 0:
        break

    print(f"CASE# {tc}:")

    marble = []
    for _ in range(N):
        num = int(input())
        marble.append(num)
    marble.sort()

    query_list = []
    for _ in range(Q):
        query = int(input())
        query_list.append(query)
    
    for num in query_list:
        if num in marble:
            print(f"{num} found at {marble.index(num) + 1}")
        else:
            print(f"{num} not found")
    
    tc += 1
# 2026.05.25 二刷
