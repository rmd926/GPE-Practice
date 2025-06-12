# 🔢 UVa 10931 - Parity
![image](https://github.com/user-attachments/assets/a0dc2b0a-fa52-4736-a82d-2e7725c10ce4)

## 📘 題目敘述

定義整數 \( n \) 的 parity 為其二進位表示中所有位元的總和再對 2 取模的結果。

例如，數字 21 的二進位是 `10101`，其中有三個 1，因此它的 parity 是 \( 3 \mod 2 = 1 \)。

本題要求計算輸入整數 \( I \) 的 parity。

---

## 💡 解題提示（Hint）

- 對每個輸入的整數 \( I \)（直到輸入為 0 結束，不需處理 0），
- 將 \( I \) 轉成二進位字串，計算字串中 '1' 的個數，
- 這個個數即為 parity 的值，
- 輸出格式為：
The parity of B is P (mod 2).
其中 \( B \) 是 \( I \) 的二進位表示，\( P \) 是該數中 1 的個數。

- 可使用 Python 的 `bin()` 函數快速轉換為二進位字串。

