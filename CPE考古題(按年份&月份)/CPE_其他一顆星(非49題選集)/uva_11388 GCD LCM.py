tc = int(input())

for _ in range(tc):
    G, L = map(int, input().split())

    if L % G == 0:
        print(G, L)
    else:
        print(-1)
