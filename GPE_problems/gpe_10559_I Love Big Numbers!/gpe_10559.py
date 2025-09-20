# import sys
# def factorial(n: int) -> int:
#     fac = [1] * (n + 1)      # fac[0] = 1
#     for i in range(1, n + 1):
#         fac[i] = fac[i - 1] * i
#     return fac[n]

# target = int(sys.stdin.readline())
# while True:
#     ans = 0
#     for num in str(factorial(target)):
#         ans += int(num)
#     print(ans)
#  TLE ==

import sys

def factorial(n: int):
    fac = [1] * (n + 1)      # fac[0] = 1
    for i in range(1, n + 1):
        fac[i] = fac[i - 1] * i
    return fac
def main():

    nums = list(map(int, sys.stdin.read().split()))
    if not nums:
        sys.exit(0)

    max_n = max(nums)
    fac = factorial(max_n)
    
    for n in nums:
        total = sum(int(n) for n in str(fac[n]))
        # total = 0
        # for i in str(fac[n]):
        #     total += int(i)
        print(total)

if __name__ == '__main__':
    main()
        # print(sum(int(d) for d in str(fac[n])))


    
