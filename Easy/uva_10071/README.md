# 🧪 UVa 10071 - Back to High School Physics
![image](https://github.com/user-attachments/assets/8f5b706e-910c-4d4a-a28a-204ae0bd0440)
---

## 📘 題目敘述

一個粒子有初速度與等加速度。如果在某段時間後它的速度為 `v`，請問：  
**在這段時間的兩倍內，它的總位移會是多少？**

---

## 💡 解題提示（Hint）

- 根據物理公式，粒子的等加速度運動中：
v = a * t -> a = v / t


- 位移公式：
s = v₀ * t + 0.5 * a * t²

- 本題已知 v 是最終速度，初速 v₀ 為 0，計算在 **2t 時間內的總位移**，可直接推導出：
s = v * t

- 只要輸入 v 和 t，輸出結果為：
displacement = 2 * v * t

