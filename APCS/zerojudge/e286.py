# https://zerojudge.tw/ShowProblem?problemid=e286

host_win = 0
for i in range(2):
    host = sum([int(i) for i in input().split()])
    guest = sum([int(i) for i in input().split()])
    if host > guest:
        host_win += 1
    print(str(host)+":"+str(guest))

if host_win == 2:
    print("Win")
elif host_win == 0:
    print("Lose")
else:
    print("Tie")