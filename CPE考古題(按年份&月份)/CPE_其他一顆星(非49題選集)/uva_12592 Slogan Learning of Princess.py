tc = int(input())
lookup = {}

for _ in range(tc):
    try:
        s1 = input()
        s2 = input()
    except:
        break

    lookup[s1] = s2

Q = int(input())
for _ in range(Q):
    target = input()
    print(lookup[target])
