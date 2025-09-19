# 24911 — Robot Instructions
<img width="772" height="896" alt="image" src="https://github.com/user-attachments/assets/4b5d174c-a611-4a04-a957-46ee7742e0d5" />


## 📘 題目敘述

有 `T` 組測資。每組先給整數 `n`，接著 `n` 行指令：

* `LEFT`：位置 `-1`
* `RIGHT`：位置 `+1`
* `SAME AS i`：與第 `i` 條指令相同（`1 ≤ i ≤ 已處理條數`）
  請輸出執行完該組 `n` 條指令後，機器人的最終位置。每組測資計算時位置先從 `0` 開始。

## 💡 解題提示（Hint）

* 以陣列保存每條指令對位置的**位移**（`-1` 或 `+1`）。
* 遇到 `SAME AS i` 時，直接取先前保存的位移 `step = hist[i-1]`。
* 注意 `i` 可能為兩位數以上，用 `split()` 解析最後一個數字字串。
* 位置為所有位移之和。時間 `O(n)`，空間 `O(n)`。

## Sample input:

```
2
3
LEFT
RIGHT
SAME AS 2
5
LEFT
SAME AS 1
SAME AS 2
SAME AS 1
SAME AS 4
```

## Sample Output:

```
1
-5
```
