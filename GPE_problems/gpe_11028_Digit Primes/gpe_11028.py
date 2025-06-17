import sys

def sieve(n):
    # initialize all entries as True (potential primes)
    is_prime = [True] * (n+1)
    # 0 and 1 are not prime
    is_prime[0] = is_prime[1] = False
    
    # only need to check up to sqrt(n)
    root = int(n ** 0.5)

    # mark multiples of each prime as non-prime
    for i in range(2, root):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    return is_prime


def digit_sum(x):
    # compute sum of decimal digits of x
    d_sum = 0
    while x:
        d_sum += x % 10
        x //= 10
    return d_sum


def main():
    data = sys.stdin.buffer.read().split()
    test_case = int(data[0])  # number of queries

    MAX = 1_000_000
    # precompute prime flags up to MAX
    all_primes = sieve(MAX)

    # dp[i] = count of numbers ≤ i that are prime and whose digit sum is prime
    dp = [0] * (MAX + 1)
    count = 0
    for i in range(MAX + 1):
        if all_primes[i] and all_primes[digit_sum(i)]:
            count += 1
        dp[i] = count

    # answer each query in O(1) via prefix sums
    output = []
    index = 1
    for _ in range(test_case):
        left = int(data[index])
        right = int(data[index + 1])
        index += 2
        # subtract dp[left-1] to include left
        output.append(str(dp[right] - dp[left-1]))

    sys.stdout.write("\n".join(output))


if __name__ == "__main__":
    main()
