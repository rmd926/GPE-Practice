# GPE 10422 — Is This Integration?
<img width="591" height="867" alt="image" src="https://github.com/user-attachments/assets/76e8c372-eec0-4008-b094-c89586f2b75c" />

## 📘 題目敘述

正方形邊長為 `a`。以四個頂點為圓心、半徑 `a` 畫四分之一圓，如圖形成三種區域：條紋區（中央的鏡片狀）、點點區（四角的弧形）、其餘區。對每筆 `a`，輸出三個面積（條紋、點點、其餘），各保留三位小數。

## 💡 解題提示（Hint）

幾何分解即可，不必做積分。令 `A = a²`：

* 角落四分之一中的「其餘區」**單象限**面積
  `corner = A * (1 - π/6 - √3/4)`
* **其餘區總面積**
  `rest = 4 * corner`
* **點點區總面積**（四角弓形）：
  `dotted = 4 * ( A*(1 - π/4) - 2*corner )`
* **條紋區面積**
  `striped = A - dotted - rest`

上式來自兩圓交疊（圓心距 `d=a`）與「扇形 − 三角形」分解。輸出順序：`striped dotted rest`。

## Sample input:

```
0.1
0.2
0.3
```

## Sample Output:

```
0.003 0.005 0.002
0.013 0.020 0.007
0.028 0.046 0.016
```
