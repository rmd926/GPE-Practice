# GPE 10528 — Light, more light
<img width="733" height="690" alt="image" src="https://github.com/user-attachments/assets/fbe89c94-d5f7-483f-9ab3-c19a617a3380" />

## 📘 題目敘述

走廊有編號 1..n 的開關燈。第 i 趟路會切換所有編號能被 i 整除的燈。初始全關。給定 `n`，問第 `n` 顆燈最後是開還是關。多筆輸入，以 `0` 結束。

## 💡 解題提示（Hint）

* 第 `k` 燈被切換的次數 = `k` 的因數個數。
* 因數通常成對出現，次數為偶數 → 最終關。只有**完全平方數**有一個未成對因數（平方根），次數為奇數 → 最終開。
* 判斷 `n` 是否完全平方：令 `r = ⌊√n⌋`，若 `r*r == n` 則輸出 `yes`，否則 `no`。

## Sample input:

```
3
6241
8191
0
```

## Sample Output:

```
no
yes
no
```
