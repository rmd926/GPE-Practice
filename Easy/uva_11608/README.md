# 11608 — No Problem!

## 📘 題目敘述

給定一年開始時已有的題數 `S`，接著兩列各 12 個整數：

* 第 2 列為每個月**新增**的題數 `make[i]`。
* 第 3 列為每個月需要使用的題數 `need[i]`。

規則：某月生產的題目只能在**之後**的月份使用；若當月可用題數不足，該月比賽取消但仍會照常生產該月的題目。
輸出格式：對每筆測資先輸出 `Case X:`，再依序輸出 12 行，當月可用題數足夠就印 `No problem! :D`，否則印 `No problem. :(`。
輸入以 `S < 0` 結束。

## 💡 解題提示（Hint）

* 逐月模擬。月序從 0..11 或 1..12。
* 當月流程：

  1. 先判斷目前可用題數 `S` 是否滿足 `need[i]`。
  2. 若足夠，輸出 `:D` 並 `S -= need[i]`；否則輸出 `:(`。
  3. 最後把本月新產生題數加入：`S += make[i]`。
* 不要用整年 `sum`；結果取決於每月是否扣除，需序貫更新。
* 複雜度 `O(12)`。

## Sample input:

```
5
3 0 3 5 8 2 1 0 3 5 6 9
0 0 10 2 6 4 1 0 1 1 2 2
-1
```

## Sample Output:

```
Case 1:
No problem! :D
No problem! :D
No problem. :(
No problem! :D
No problem! :D
No problem! :D
No problem! :D
No problem! :D
No problem! :D
No problem! :D
No problem! :D
No problem! :D
```
