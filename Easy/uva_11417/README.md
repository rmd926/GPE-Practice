# 🔢 UVa 11417 - GCD

![image](https://github.com/user-attachments/assets/122445a5-0ff6-4aaa-a901-0d084376698b)

![image](https://github.com/user-attachments/assets/02d20530-9fdf-4b4d-9174-bb066bb8b3b0)

## 📘 題目敘述

給定一個整數 \( N \)，求以下數值 \( G \)：

\[
G = \sum_{i=1}^{N} \sum_{j=i+1}^{N} \gcd(i, j)
\]

其中，\(\gcd(i, j)\) 是整數 \( i \) 與 \( j \) 的最大公因數。

輸入包含多組測試資料，每行為一個整數 \( N \)（\(1 < N < 501\)），輸入以 0 結束（不需處理該行）。

---

## 💡 解題提示（Hint）

- 使用兩層迴圈計算所有 \(1 \leq i < j \leq N\) 的最大公因數並累加。  
- 可利用 Python 的 `math.gcd()` 函數快速求最大公因數。  
- 注意輸入結束條件為 0。  
- 輸出每組輸入對應的 \( G \) 值。

