# 11185 — Ternary
<img width="688" height="528" alt="image" src="https://github.com/user-attachments/assets/44716070-e742-4a9e-b993-35d3fed8a5b3" />

## 📘 題目敘述

輸入多行十進位整數 `N`（`0 ≤ N < 1e9`）。每行輸出其**三進位**表示。遇到負數行結束，不輸出該行。

## 💡 解題提示（Hint）

* 反覆除以 3，收集餘數（0、1、2），倒序即為三進位字串。
* 特判 `N = 0` 應輸出 `0`。
* 多筆輸入直到遇到負數。

## Sample input:

```
10
100
1000
-1
```

## Sample Output:

```
101
10201
1101001
```
