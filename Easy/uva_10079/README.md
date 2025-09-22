# uva 10079 — Pizza Cutting
![Uploading image.png…]()

## 📘 題目敘述

給一個整數 `N`（多筆，逐行），代表對披薩做 `N` 次**直線**切割。請輸出最多能切出的片數。輸入遇到負數結束，不處理該行。

## 💡 解題提示（Hint）

最多片數是經典的 **Lazy Caterer’s sequence**：

$$
\text{pieces}(N)=1+\frac{N(N+1)}{2}.
$$

理由：第 `i` 刀最多與先前 `i-1` 刀各相交一次，新增 `i` 片；累加得上式。注意使用 64-bit 整數（`N ≤ 2.1e9`）。

## Sample input:

```
5
10
-100
```

## Sample Output:

```
16
56
```
