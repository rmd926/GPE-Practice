# 📐 UVa 11461 - Square Numbers
![image](https://github.com/user-attachments/assets/11fe22bf-e813-4b7a-b9a3-f987a06bd54b)

## 📘 題目敘述

一個「平方數（square number）」是其平方根也是整數的數字，例如：1、4、81 都是平方數。

給定兩個整數 `a` 與 `b`，請找出在區間 `[a, b]`（含 `a` 和 `b`）之間有多少個平方數。

---

## 💡 解題提示（Hint）

- 本題要求找出所有滿足條件的整數 `x`，使得 `x²` 在 `[a, b]` 範圍內。
- 可轉換為：找出 `sqrt(a)` 向上取整 到 `sqrt(b)` 向下取整 之間有多少整數。
- 實作步驟如下：
  1. 計算 `ceil(sqrt(a))` 與 `floor(sqrt(b))`
  2. 若範圍合法，答案為 `floor(sqrt(b)) - ceil(sqrt(a)) + 1`
  3. 若 `a > b` 或無平方數符合條件，則答案為 `0`
- 結尾條件為讀入 `0 0`，不處理此筆輸入。
- 注意處理多組輸入資料，可使用 `while` 搭配 `break` 判斷結束。

---
