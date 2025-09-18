# 10018 — Reverse and Add
<img width="507" height="652" alt="image" src="https://github.com/user-attachments/assets/823dc204-a7ab-4ce2-a392-42bfaf379b85" />

## 📘 題目敘述

給一個正整數 `P`。重複進行：把 `P` 的數字反轉成 `rev(P)`，令 `P = P + rev(P)`。
若 `P` 非回文（正反讀相同），就繼續上述步驟；若為回文則停止。
對每筆輸入，輸出「進行了幾次加法」以及「最後得到的回文數」。

## 💡 解題提示（Hint）

* 以字串判斷回文最直觀：`s == s[::-1]`。
* 反轉可用：`rev = int(str(n)[::-1])`。
* 迭代累加並計數，直到成為回文為止。
* 題目保證每筆資料在 **< 1000 次** 加法內會得到答案，且結果不超過 `4,294,967,295`。
* 複雜度：約 `O(k·D)`，`k` 為加法次數，`D` 為位數。

**Python 範例**

```python
def is_pal(n: int) -> bool:
    s = str(n)
    return s == s[::-1]

def solve_one(p: int):
    cnt = 0
    while not is_pal(p):
        p += int(str(p)[::-1])
        cnt += 1
    return cnt, p

t = int(input())
for _ in range(t):
    p = int(input())
    c, ans = solve_one(p)
    print(c, ans)
```

## Sample input:

```
3
195
265
750
```

## Sample Output:

```
4 9339
5 45254
3 6666
```
