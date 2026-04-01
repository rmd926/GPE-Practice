MAX = 50
dp = [0] * (MAX+1)
dp[0], dp[1], dp[2] = 0, 1, 2

for i in range(3, MAX+1):
	dp[i] = dp[i-1] + dp[i-2]

while True:
	try:
		n = int(input())
	except:
		break
        
	if n == 0:
        break
    
    print(dp[n])

# 瘋狂程設的code
MAX = 50
dp = [0] * (MAX+1)
dp[0], dp[1], dp[2] = 0, 1, 2

for i in range(3, MAX+1):
	dp[i] = dp[i-1] + dp[i-2]

while True:
	try:
		target = list(map(int, input().split()))
	except:
		break
	
	for i in range(len(target)):
		if target[i] == 0:
			break
		else:
			print(dp[target[i]])
