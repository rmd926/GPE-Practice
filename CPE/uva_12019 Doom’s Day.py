options = ["Friday", "Saturday", "Sunday","Monday", "Tuesday", "Wednesday", "Thursday"]
days = [0,31,28,31,30,31,30,31,31,30,31,30,31] #0: dummy
# print(sum(days[0:2]))
tc = int(input())

for i in range(tc):
    M, D = map(int, input().split())
    ans = sum(days[0:M]) + D
    print(options[ans%7])
