# 先建表，因為存在100個循環之規律
# 切記需要只留個位數去做計算，避免過多位數造成TLE
table = [0] * 101
for num in range(1, 101):
	table[num] += ((num ** num) % 10 + table[num-1]) % 10

while True:
	target = int(input())
	if target == 0:
		break
	print(table[target % 100])
