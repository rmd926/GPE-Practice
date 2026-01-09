'''
因為0 <= a <= b <= 10000，所以就是用建表的方式做。
此外，因為要算機率，需要知道True有幾個，所以可以使用count或者是把True的在list內都改成1，然後取sum除以總數量
最後就是注意機率要先*100再把格式改成小數點後2位即可
'''
MAX = 10000
prime_list = [0] * (MAX+1)

def is_prime(n):
	if n <= 1:
		return False
	for i in range(2, int(n ** 0.5) + 1):
		if n % i == 0:
			return False
	return True

for i in range(MAX + 1): # create tables
	if is_prime(i**2 + i + 41):
		prime_list[i] = 1
	else:
		prime_list[i] = 0
	
while True:
	a, b = map(int, input().split())
	prime_times = sum(prime_list[a:b+1])
	
	ans = 100 * prime_times / (b-a+1)
	print(f"{ans:.2f}")

