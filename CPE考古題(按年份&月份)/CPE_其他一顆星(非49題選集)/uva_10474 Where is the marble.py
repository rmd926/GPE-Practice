tc = 1
while True:
    N, Q = map(int, input().split())
    if N == 0 and Q == 0:
        break
    
    target = []
    for _ in range(N):
        num = int(input())
        target.append(num)
    target.sort()
    
    query_list = []
    for _ in range(Q):
        query = int(input())
        query_list.append(query)
    
    print(f"CASE# {tc}:")
    
    for num in query_list:
        if num in target:
            print(f"{num} found at {target.index(num) + 1}")
        else:
            print(f"{num} not found")
    
    tc += 1
