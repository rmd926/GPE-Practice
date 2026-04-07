tc = int(input())
for _ in range(tc):
    target = int(input())
    ans = ((abs((((((target*63)+7492)*235)//47)-498))//10)%10)
    print(ans)
