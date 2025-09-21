# GPE 10500 — Brick Wall Patterns

<img width="589" height="841" alt="image" src="https://github.com/user-attachments/assets/67d4dfc7-7e49-403d-a707-f8a20a4667fd" />
## 📘 題目敘述

牆高固定為 2。可用兩種磚：

* 直立 1×2（佔寬 1）
* 橫放 2×1（佔寬 2）

給定牆的長度 `n`（寬度），問有多少種鋪法。輸入為多筆 `n`，以 `0` 結束；每筆輸出對應的鋪法數。

## 💡 解題提示（Hint）

狀態轉移：

* `f(0)=1`（空牆一種）
* `f(1)=1`（只能直立一塊）
* `f(n)=f(n-1)+f(n-2)`
  解釋：最後一格放直立磚 → 剩 `n-1`；最後兩格放橫磚疊成一列 → 剩 `n-2`。
  這就是 Fibonacci，計到 `n` 即可。多筆輸入逐行輸出。

## Sample input:

```
1
2
3
0
```

## Sample Output:

```
1
2
3
```
