#!/usr/bin/env python3

def sieve_primes(limit):
    """回傳 ≤ limit 的所有質數列表。"""
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, limit + 1, i):
                is_prime[j] = False
    return [i for i, flag in enumerate(is_prime) if flag]

# 事先篩出所有 ≤10000 的質數
PRIMES = sieve_primes(10000)

def count_consecutive_prime_sums(n):
    """
    計算有多少種方法，能將 n 表示成「一段或多段連續質數的和」。
    使用「雙指標＋滑動視窗」技巧，時間複雜度 O(P)，P = 質數個數。
    """
    count = 0
    left = 0
    right = 0
    current_sum = 0
    L = len(PRIMES)

    while True:
        # 先檢查目前的視窗和是否等於 n
        if current_sum == n:
            count += 1
        # 若目前和 ≥ n，就往左收縮
        if current_sum >= n:
            current_sum -= PRIMES[left]
            left += 1
        else:
            # current_sum < n，嘗試往右擴張
            if right == L:
                break
            current_sum += PRIMES[right]
            right += 1

    return count

def main():
    try:
        while True:
            line = input().strip()
            if not line:
                continue
            n = int(line)
            if n == 0:
                break
            # 對每個 n 輸出表示數量
            print(count_consecutive_prime_sums(n))
    except EOFError:
        pass

if __name__ == "__main__":
    main()
