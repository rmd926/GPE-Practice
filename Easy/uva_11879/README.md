# 11879 — Multiple of 17

## 📘 題目敘述

輸入多行整數 `n`（`1 ≤ n ≤ 10^100`），以 `0` 結束且不處理。
對每行 `n`，判斷是否為 **17 的倍數**：是輸出 `1`，否輸出 `0`。

## 💡 解題提示（Hint）

* 數字可非常大，建議**字串逐位取餘**：
  `rem = 0; rem = (rem*10 + digit) % 17`，掃完整串後看 `rem==0`。
* 也可用定理（去尾位法）：將末位數字 `d` 取出，計算 `new = remaining - 5*d`，重複直到數字小而易判。
* 時間複雜度 `O(len(n))`，空間 `O(1)`。
* 最tricky methods直接取mod幹下去結束 ^^
* 參考實作（Python）：

  ```python
  import sys
  out = []
  for s in sys.stdin.read().split():
      if s == '0': break
      r = 0
      for ch in s:
          r = (r * 10 + (ord(ch) - 48)) % 17
      out.append('1' if r == 0 else '0')
  print('\n'.join(out))
  ```

## Sample input:

```
34
201
2098765413
1717171717171717171717171717171717171717171718
0
```

## Sample Output:

```
1
0
1
0
```
