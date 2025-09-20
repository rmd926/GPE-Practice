# GPE 24681 — Perfection

## 📘 題目敘述

輸入多個正整數 `n`（`n ≤ 60000`），以 `0` 結束且不處理。對每個 `n` 判斷其為：

* **PERFECT**：正因數（不含自己）總和等於 `n`
* **ABUNDANT**：總和大於 `n`
* **DEFICIENT**：總和小於 `n`

輸出格式固定：第一行印 `PERFECTION OUTPUT`，其後每行將 `n` 以**寬度 5 右對齊**列出，接兩個空白與分類字串。最後一行印 `END OF OUTPUT`。

## 💡 解題提示（Hint）

* 計算正因數和時，只需枚舉到 `√n`。成對加入 `i` 與 `n/i`，記得排除 `n` 本身並處理平方數去重。
* 特例：`n=1`，因數和為 `0`。
* 複雜度：對每個 `n` 為 `O(√n)`。

**參考實作（Python）**

```python
import sys
nums = list(map(int, sys.stdin.read().split()))
print("PERFECTION OUTPUT")
for n in nums:
    if n == 0:
        break
    s = 1 if n > 1 else 0
    i = 2
    while i * i <= n:
        if n % i == 0:
            s += i
            if i * i != n:
                s += n // i
        i += 1
    kind = "PERFECT" if s == n else ("ABUNDANT" if s > n else "DEFICIENT")
    print(f"{n:>5}  {kind}")
print("END OF OUTPUT")
```

## Sample input:

```
15 28 6 56 60000 22 496 0
```

## Sample Output:

```
PERFECTION OUTPUT
   15  DEFICIENT
   28  PERFECT
    6  PERFECT
   56  ABUNDANT
60000  ABUNDANT
   22  DEFICIENT
  496  PERFECT
END OF OUTPUT
```
