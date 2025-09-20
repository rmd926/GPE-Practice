# GPE 10559 — I Love Big Numbers!
<img width="711" height="880" alt="image" src="https://github.com/user-attachments/assets/046d577c-7a54-47f1-ac0c-fe842c9fbdb7" />

## 📘 題目敘述

給定整數 `n (n ≤ 1000)`，計算 `n!`，再輸出 `n!` 的數位和。輸入包含一個或多個測資，每行一個 `n`；逐行輸出答案。

## 💡 解題提示（Hint）

* 直接算 `n!` 再把字串各位數相加即可。
* 多筆測資建議先讀完，找出最大 `n`，**自底向上**一次累乘到 `max_n`，把每個 `i!` 的數位和存表，查表輸出。
* Python 可用內建大整數；其他語言可用大數陣列或庫。
* 複雜度：約 `O(max_n · 位數(n!))`，每筆查詢 `O(1)`。

**參考 Python**

```python
import sys

nums = [int(s) for s in sys.stdin.read().split()]
if nums:
    mx = max(nums)
    fact = 1
    digit_sum = [0]*(mx+1)
    for i in range(1, mx+1):
        fact *= i
        digit_sum[i] = sum(map(int, str(fact)))
    for n in nums:
        print(digit_sum[n])
```

## Sample input:

```
5
60
100
```

## Sample Output:

```
3
288
648
```
