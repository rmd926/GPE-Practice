# 🔢 UVa 10235 - Simply Emirp
![image](https://github.com/user-attachments/assets/fd45d9f4-d63f-4c3c-bea8-f94ce397edc6)

## 📘 題目敘述

整數 N（大於 1）稱為質數（prime），若其正因數只有 1 與 N 本身。  
質數在數學中扮演重要角色，且廣泛應用於密碼學與編碼理論。

Emirp（prime 倒過來拼寫）指的是一種特殊質數：  
將其位數反轉後仍為不同的質數。例如 17 和 71 都是質數，且互為反轉數，故 17 是 Emirp。

本題需判斷輸入數字 N 的類型，輸出結果為：  
1. 如果 N 非質數，輸出 "`N is not prime.`"  
2. 如果 N 是質數且不是 Emirp，輸出 "`N is prime.`"  
3. 如果 N 是 Emirp，輸出 "`N is emirp.`"

N 範圍為 1 < N < 1,000,000。

---

## 💡 解題提示（Hint）

- 實作一個質數判斷函數以檢驗 N 是否為質數。  
- 若 N 是質數，將 N 反轉成另一個數字 revN。  
- 若 revN 也為質數且 revN != N，則 N 是 Emirp。  
- 注意排除回文質數（如 131），它們不算 Emirp。  
- 輸入為多行多個 N，逐行判斷並輸出結果。

