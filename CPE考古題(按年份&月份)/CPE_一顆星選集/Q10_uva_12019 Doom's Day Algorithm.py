tc = int(input())
day = ["Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for _ in range(tc):
	month, date = map(int, input().split())
	total_days = sum(month_days[0: month]) + date
	
	print(day[total_days % 7])
