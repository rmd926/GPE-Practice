# 12015 — Google is Feeling Lucky

## 📘 題目敘述

每筆測資有 10 行，包含一個網址與其整數相關度 `V`。請輸出**相關度最高**的所有網址，並維持**輸入順序**。每筆測資前需印 `Case #x:`。測資數 `T` 由第一行給定。

## 💡 解題提示（Hint）

* 對每筆測資讀入 10 組 `(url, v)`。
* 取得 `maxV = max(v)`，再依讀入順序輸出所有 `v == maxV` 的 `url`。
* 請勿排序。時間與空間皆為 O(10)。

## Sample input:

```
2
www.youtube.com 1
www.google.com 2
www.google.com.hk 3
www.alibaba.com 10
www.taobao.com 5
www.bad.com 10
www.good.com 7
www.fudan.edu.cn 8
www.university.edu.cn 9
acm.university.edu.cn 10
www.youtube.com 1
www.google.com.hk 3
www.google.com 2
www.alibaba.com 10
www.taobao.com 5
www.good.com 7
www.fudan.edu.cn 8
www.university.edu.cn 9
acm.university.edu.cn 9
www.bad.com 6
```

## Sample Output:

```
Case #1:
www.alibaba.com
www.bad.com
acm.university.edu.cn
Case #2:
www.alibaba.com
```
