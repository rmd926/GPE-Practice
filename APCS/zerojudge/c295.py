# https://zerojudge.tw/ShowProblem?problemid=c295
line, length = map(int, input().split()) # 行數、每行長度
ans = 0
temp = [0] * line

for i in range(line):
	content = [int(x) for x in input().split()] # 每行list的內容
	i_max = max(content)
	temp[i] = i_max
	ans = sum(temp)

print(ans)
factor = []
for num in temp:
	if ans % num == 0:
		factor.append(num)
if factor == []:
	print(-1)
else:
	print(*factor)