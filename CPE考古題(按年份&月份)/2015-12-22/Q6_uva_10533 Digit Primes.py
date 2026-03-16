MAX = 10 ** 6
is_prime = [True] * (MAX+1)
is_prime[0] = is_prime[1] = False
for i in range(2, int(MAX**0.5)+1):
	if is_prime[i]:
		for j in range(i**2, MAX+1, i):
			is_prime[j] = False

def digit_sum(num):
	result = 0
	for char in str(num):
		result += int(char)
	return result		

tc = int(input())
for _ in range(tc):
	low, high = map(int, input().split())
	count = 0
	for num in range(low, high+1):
		if is_prime[num] and is_prime[digit_sum(num)]:
			count += 1
	print(count)
