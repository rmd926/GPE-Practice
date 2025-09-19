# GPE 11006 — Rank the Languages

## 📘 題目敘述

給一張 `H×W` 地圖，每格是小寫字母，代表一種語言。**州**定義為同字母且以**上下左右**相連的連通塊。
對每筆測資，輸出各語言的州數，排序規則為：州數**遞減**，若相同則以字母**遞增**。每筆開頭先印 `World #k`。

約束：`1 ≤ H,W ≤ 20`，多筆測資。

## 💡 解題提示（Hint）

* 對每個未處理的格子啟動一次 Flood Fill（DFS/BFS，四方向）。
* 啟動時對該字母計數 +1，並將整塊標記為已訪（可就地改寫或用 visited）。
* 可選：外圍包一圈哨兵，省去邊界判斷。
* 複雜度 `O(HW)`。

## Sample input:

```
2
4 8
ttuuttdd
ttuuttdd
uuttuudd
uuttuudd
9 9
bbbbbbbbb
aaaaaaaab
bbbbbbbab
baaaaacab
baccccacb
bacbbbacb
baccccacb
baaaaaaab
bbbbbbbbb
```

## Sample Output:

```
World #1
t: 3
u: 3
d: 1
World #2
b: 2
a: 1
c: 1
```
