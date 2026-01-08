tc = int(input())
x = 0
for _ in range(tc):
    input()
    index = list(map(int,input().split()))
    data = list(map(str, input().split()))

    ans = {}

    for i in range(len(index)):
        ans[index[i]] = data[i]

    if x > 0:
        print()

    x += 1

    for key in sorted(ans):
        print(ans[key])