# 10409 — Die Game
<img width="680" height="812" alt="image" src="https://github.com/user-attachments/assets/e4d81794-d3aa-4663-befc-0a2235dc6e52" />

## 📘 題目敘述

給一串指令（每筆一局）：`north | south | east | west`。
初始骰子朝向固定，面標為 1..6，對面相加為 7；初始六面為：

* top=1, bottom=6, north=2, south=5, west=3, east=4
  依序執行指令，輸出最後的 **top**。

## 💡 解題提示（Hint）

模擬轉動即可。維護三面就夠（top、north、west），其餘由對面=7−face 得出。
更新規則（一次一指令）：

```text
north: top, north, south, bottom ← south, top, bottom, north
south: top, north, south, bottom ← north, bottom, top, south
west : top, west,  east,  bottom ← east,  top,   bottom, west
east : top, west,  east,  bottom ← west,  bottom, top,   east
```

時間 O(指令數)，空間 O(1)。

## Sample input:

```
1
north
3
north
east
south
0
```

## Sample Output:

```
5
1
```
