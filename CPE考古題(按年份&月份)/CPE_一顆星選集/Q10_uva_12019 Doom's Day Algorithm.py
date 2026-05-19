tc = int(input())
Day = ["Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for _ in range(tc):
	month, day = map(int, input().split())
	total = sum(month_days[0: month]) + day
	
	print(Day[total % 7])

# 2026.05.19 二刷
