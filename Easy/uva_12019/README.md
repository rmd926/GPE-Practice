# 📅 UVa 12019 - Doom’s Day Algorithm
![image](https://github.com/user-attachments/assets/18318650-079b-4228-bb0c-6329eee2836f)

## 📘 題目敘述

Doom's Day 演算法由 John Conway 創立，用於計算任意日期為星期幾。  
該算法根據每年「Doomsday」的日期來判斷星期幾，Doomsday 是某年中總落在同一星期幾的特殊日期集合。

2011 年的 Doomsday 包括：  
- 4/4、6/6、8/8、10/10、12/12  
- 其他特定日期如 5/9、7/11、11/7 等  
- 閏年額外有 1/11 與 2/22

給定 2011 年的某月日，請判斷該日是星期幾。

---

## 💡 解題提示（Hint）

- 先找出 2011 年的 Doomsday 星期幾（題目中已隱含，可用表列法處理）。  
- 使用日期差值與 Doomsday 日期計算目標日期星期幾。  
- 注意閏年影響及特殊 Doomsday 日期。  
- 使用星期循環（Monday~Sunday）模擬計算。  
- 輸入多組測資，輸出對應星期名稱。

## Sample input: 

- 8
- 1 6
- 2 28
-4 5
-5 26
-8 1
-11 1
-12 25
-12 31

## Sample Output: 

-Thursday
-Monday
-Tuesday
-Thursday
-Monday
-Tuesday
-Sunday
-Saturday
