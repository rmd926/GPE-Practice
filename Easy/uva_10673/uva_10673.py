# import math

# TC = int(input())
# for _ in range(TC):
#     x, k = map(int, input().split())

#     a = math.floor(x / k)
#     b = math.ceil(x / k)
#     r = x - a * k  # = x % k

#     if r == 0:              # a == b
#         p, q = 0, k
#     else:                   # b = a + 1
#         p, q = k - r, r

#     print(p, q)
# # import math
# # print(math.ceil(40/2))

n = int(input())
for i in range(n):
	x, k = map(int, input().split())
	
	print("{} {}".format(k - x%k, x%k))