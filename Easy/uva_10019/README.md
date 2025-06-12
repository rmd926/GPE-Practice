# 🔐 UVa 10019 - Funny Encryption Method
![image](https://github.com/user-attachments/assets/cd7f58e6-3a0e-473c-ac8c-82709a8ae310)
![image](https://github.com/user-attachments/assets/30dbe988-a09c-4db9-8a5e-f7cb45ccc7c3)

## 📘 題目敘述

一名學生在 ITESM Campus Monterrey 使用一種新的加密方法處理數字。  
該方法包含以下步驟：

1. 讀取一個十進位數字 \( M \)。
2. 將 \( M \) 轉成二進位表示，計算其中 1 的數量為 \( b_1 \)。
3. 將 \( M \) 視為十六進位數字，轉成二進位表示，計算其中 1 的數量為 \( b_2 \)。
4. 最終加密結果為 \( M \oplus (b_1 \times b_2) \)，其中 \(\oplus\) 為 XOR 運算。

請撰寫程式，讀入多組數字 \( M \)，輸出每組數字在二進位及十六進位表示中 1 的數量 \( b_1 \) 和 \( b_2 \)。

---

## 💡 解題提示（Hint）

- 對每個輸入的十進位數字 \( M \)：
  - 計算其二進位表示中 '1' 的數量 \( b_1 \)。
  - 將 \( M \) 轉換為十六進位字串，再將該十六進位字串視為一個十六進位數，轉成二進位，計算其中 '1' 的數量 \( b_2 \)。
- Python 中可以用 `bin()` 函數求二進位表示，用 `hex()` 取得十六進位表示。
- 輸出格式為兩個整數 \( b_1 \) 和 \( b_2 \)，以空白分隔。




