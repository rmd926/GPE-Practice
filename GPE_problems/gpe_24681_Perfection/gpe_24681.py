# import sys
# nums = list(map(int, sys.stdin.read().split()))
# print("PERFECTION OUTPUT")
# for n in nums:
#     if n == 0:
#         break
#     s = 1 if n > 1 else 0
#     i = 2
#     while i * i <= n:
#         if n % i == 0:
#             s += i
#             if i * i != n:
#                 s += n // i
#         i += 1
#     kind = "PERFECT" if s == n else ("ABUNDANT" if s > n else "DEFICIENT")
#     print(f"{n:>5}  {kind}")
# print("END OF OUTPUT")


# noob method
import sys

def find_factors_sum(n):
    fac_sum = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            fac_sum += i
    return fac_sum

def classify(n: int) -> str:
    s = find_factors_sum(n)
    if s == n:  return "PERFECT"
    if s > n:   return "ABUNDANT"
    return "DEFICIENT"

def main():
    print("PERFECTION OUTPUT")
    for tok in sys.stdin.read().split():
        n = int(tok)
        if n == 0:
            break
        print(f"{n:>5}  {classify(n)}")
    print("END OF OUTPUT")

if __name__ == "__main__":
    main()
