# 12372 — Packing for Holiday
<img width="676" height="833" alt="image" src="https://github.com/user-attachments/assets/8f3bd718-e64a-4625-8bd8-32f20874b254" />

## 📘 題目敘述

Mr. Bean 想確認禮物盒能否放進長寬高皆為 **20 英吋** 的行李箱。每次給你一個長方體盒子的三邊長 `L, W, H`（邊需與行李箱邊平行），請判斷是否能放入。

輸入第一行為測資數 `T (T ≤ 100)`，接著 `T` 行各含三個整數 `L, W, H (1 ≤ L, W, H ≤ 50)`。

對每組輸出 `Case i: good` 若能放入；否則輸出 `Case i: bad`。

## 💡 解題提示（Hint）

* 只需檢查三邊是否都 `≤ 20`。
* 不用考慮旋轉到非平行方向；題目限制邊與箱子邊平行。

## Sample input:

```
2
20 20 20
1 2 21
```

## Sample Output:

```
Case 1: good
Case 2: bad
```
