tc = int(input())
ans = 0

for _ in range(tc):
    try:
        opt = input()
    except:
        break

    if opt == "report":
        print(ans)

    else:
        donate = int(opt.split()[-1])
        ans += donate
