tc = int(input())
for _ in range(tc):
    n = int(input())
    ans = 0          # 最後答案：H(n) = sum(n // i)
    i = 1            # 從 i = 1 開始枚舉

    while i <= n:
        q = n // i   # 當前這一段的值（floor(n / i)）

        # 找到「最後一個 j」，使得 n // j 仍然等於 q
        # 也就是這一整段 [i, last] 的值都一樣是 q
        last = n // q
        # 這一段共有 (last - i + 1) 個 i
        # 每個的值都是 q，所以一次加總
        ans += q * (last - i + 1)

        # 直接跳到下一段（避免一個一個跑）
        i = last + 1

    print(ans)
