# 113 — Power of Cryptography
<img width="711" height="708" alt="image" src="https://github.com/user-attachments/assets/63f8bc37-74bd-4867-955d-bffe89dc63af" />

## 📘 題目敘述

給定整數 `n ≥ 1` 與大整數 `p ≥ 1`，已知存在整數 `k` 使得

$$
k^n = p.
$$

請求出此 `k`。輸入包含多組資料，每組兩行依序為 `n`、`p`，到 EOF 結束。保證解 `k` 為整數，且 `1 ≤ n ≤ 200`、`1 ≤ p < 10^101`、`1 ≤ k ≤ 10^9`。

## 💡 解題提示（Hint）

* 直接用實數：`k ≈ round(p ** (1/n))`；為避免誤差，可先用 `math.pow` 或 `decimal` 求近似後四捨五入。
* 或整數二分搜尋 `k`，檢查 `k^n` 與 `p` 的關係（用快速冪，並在超過 `p` 時提早停止）。
* Python 可用 `int(Decimal(p) ** (Decimal(1)/n))` 再調整到正確整數；C++ 可用 `pow` 後微調。

## Sample input:

```
2
16
3
27
7
4357186184021382204544
```

## Sample Output:

```
4
3
1234
```
