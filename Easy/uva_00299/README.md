# 🚂 UVa 299 - Train Swapping
![image](https://github.com/user-attachments/assets/ed78807e-bd49-45a1-868b-8ae0db7a333e)
![image](https://github.com/user-attachments/assets/de124ddb-2a77-4b20-bfdf-ca093fb45b22)

## 📘 題目敘述

在一個老舊的鐵路車站，仍然可以見到「train swappers」（列車調換工）這個職業。  
列車調換工的工作是將車廂重新排列成最理想的順序。  
現在希望自動化此程序，計算將一組車廂排序所需的最少相鄰交換次數。

---

## 💡 解題提示（Hint）

- 題目本質為計算排列的「逆序數」（inversion count），即需要多少次相鄰元素交換才能排序。  
- 對輸入的車廂排列序列，計算所有 i < j 且 arr[i] > arr[j] 的對數量。  
- 可使用雙重迴圈或更有效率的合併排序法計算逆序數。  
- 輸入多組測資，輸出格式為：  Optimal train swapping takes S swaps. 其中 S 為逆序數。

