# 建立一個空的 list，用來存放每一行輸入的字串
lines = []
while True:
    try:
        sentence = input()       
        lines.append(sentence)      
    except:                         
        break

# 計算輸入的行數
num_lines = len(lines)

# 找出最長字串的長度，因為旋轉後要知道要印幾列
max_length = 0
for st in lines:
    max_length = max(max_length, len(st))

# 開始輸出旋轉後的結果
# 外層迴圈 i：控制「第 i 個字元位置」(列)
for i in range(max_length):
    # 內層迴圈 j：從最後一行開始往前 (逆時針旋轉的效果)
    for j in range(num_lines - 1, -1, -1):
        # 如果這一行有第 i 個字元，就印出來
        if i < len(lines[j]):
            print(lines[j][i], end="")
        # 如果這一行太短，沒有第 i 個字元，就補空格
        else:
            print(" ", end="")
    # 每一列印完後換行
    print()
