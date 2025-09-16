# 494 — Kindergarten Counting Game
<img width="661" height="514" alt="image" src="https://github.com/user-attachments/assets/1400e52f-e974-4f3e-abf7-6454efe13d7d" />

## 📘 題目敘述
輸入為多行文字（直到 EOF）。**word** 定義為一段連續的英文字母（A–Z 或 a–z）。  
對於輸入的每一行，輸出該行的 word 數，各行各印一個整數。

## 💡 解題提示（Hint）
- 掃描每行字元，維護布林變數 `in_word`。
- 當由「非字母」進入「字母」時，計數 +1，並設 `in_word=True`；遇到非字母則設為 `False`。
- 只將 A–Z/a–z 視為字母，避免 `isalpha()` 的 Unicode 擴張影響。
- 複雜度：每行 O(L)，額外空間 O(1)。


## Sample input:
Meep Meep!  
I tot I taw a putty tat.  
I did! I did! I did taw a putty tat.  
Shssssssssh ... I am hunting wabbits. Heh Heh Heh Heh ...  

## Sample Output:
2  
7  
10  
9  
