# 10501 — Safe Salutations
<img width="905" height="665" alt="image" src="https://github.com/user-attachments/assets/dc558736-39ef-4ed7-a936-ecf3a700523d" />

## 📘 題目敘述

有 `n` 對人（共 `2n` 人）圍成一圈要兩兩握手，要求所有連線**不相交**。給定多筆測資（每筆一個 `n`，資料集間以空行分隔），輸出可行握手數。測資之間輸出需空一行。`1 ≤ n ≤ 10`。

## 💡 解題提示（Hint）

* 問題等價於「圓上 `2n` 個點的不相交配對數」，即第 `n` 個 **Catalan 數**。
* 遞迴：

  $$
  C_0=1,\quad C_n=\sum_{k=1}^{n} C_{k-1}C_{n-k}
  $$
* 閉式：

  $$
  C_n=\frac{1}{n+1}\binom{2n}{n}
  $$
* 以大整數運算；多筆輸入，答案間印空行。

## Sample input:

```
4
```

## Sample Output:

```
14
```
