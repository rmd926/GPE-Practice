from bisect import bisect_left, bisect_right

MAX = 10**12
is_prime = [True] * (int(MAX**0.5)+1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(MAX**0.5)+1):
	if is_prime[i]:
		for j in range(i**2, int(MAX**0.5)+1, i):
			is_prime[j] = False

almost_prime = []
for i in range(2, int(MAX**0.5)+1):
	if is_prime[i]:
		x = i**2 # 檢查所有質數的n次方是否<= MAX，若有把他加到almost_prime
		while x <= MAX:
			almost_prime.append(x)
			x *= i
			
almost_prime.sort()
			
tc = int(input())
for _ in range(tc):
	low, high = map(int, input().split())
	print(bisect_right(almost_prime, high) - bisect_left(almost_prime, low))
		
