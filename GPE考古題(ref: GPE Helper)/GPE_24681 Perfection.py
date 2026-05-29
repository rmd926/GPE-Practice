MAX = 60000
is_prime = [True] * (MAX+1)
is_prime[0] = is_prime[1] = False
for i in range(2, int(MAX**0.5)+1):
    if is_prime[i]:
        for j in range(i**2, MAX+1, i):
            is_prime[j] = False

def factor_sum(num):
    ans = 0
    for i in range(1, num//2 + 1):
        if num % i == 0:
            ans += i
    return ans

print("PERFECTION OUTPUT")
while True:
    try:
        target = list(map(int, input().split()))
    except:
        break

    for num in target:
        if num == 0:
            break
        if factor_sum(num) == num:
            print(f"{num:5d}  PERFECT")
        elif factor_sum(num) > num:
            print(f"{num:5d}  ABUNDANT")
        elif factor_sum(num) < num:
            print(f"{num:5d}  DEFICIENT")

print("END OF OUTPUT")
