# uva 10673 — Play with Floor and Ceil
<img width="680" height="707" alt="image" src="https://github.com/user-attachments/assets/341bd6d7-448f-471d-9440-4e416fa15ef9" />

## 📘 題目敘述

給定兩個正整數 `x` 與 `k`，需找出整數 `p`、`q` 使得：

$$
x = p\left\lfloor\frac{x}{k}\right\rfloor \;+\; q\left\lceil\frac{x}{k}\right\rceil .
$$

輸入第一行為測試數 `T`（`1 ≤ T ≤ 1000`），接著 `T` 行每行兩個整數 `x, k`（皆 < `1e8`）。對每組輸出一組可行的 `p q`。可有多組答案，任取一組，但請確保
$p\left\lfloor\frac{x}{k}\right\rfloor$ 與 $q\left\lceil\frac{x}{k}\right\rceil$ 皆可放入 64 位帶號整數。

## 💡 解題提示（Hint）

令

$$
a=\left\lfloor \frac{x}{k}\right\rfloor,\quad b=\left\lceil \frac{x}{k}\right\rceil,\quad r=x-ak\;(=x\bmod k).
$$

* 若 `r = 0`，則 `a = b = x/k`，取 `p=0, q=k`（或任意 `p+q=k`）即可。
* 若 `r > 0`，則 `b = a + 1`，取

$$
p = k-r,\quad q=r,
$$

則 $(k-r)a + r(a+1) = ka + r = x$。

實作只需一次整除與一次取餘。

## Sample input:

```
3
5 2
40 2
24444 6
```

## Sample Output:

```
1 1
1 1
0 6
```
