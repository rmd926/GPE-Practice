options = ["Friday", "Saturday", "Sunday","Monday", "Tuesday", "Wednesday", "Thursday"]
days = [0,31,28,31,30,31,30,31,31,30,31,30,31]
tc = int(input())

for _ in range(tc):
	M, D = map(int, input().split())
	total_days = sum(days[0:M]) + D
	print(options[total_days%7])
