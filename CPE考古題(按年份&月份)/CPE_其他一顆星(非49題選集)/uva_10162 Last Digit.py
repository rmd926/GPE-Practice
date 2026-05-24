# 先建表，因為存在100個循環之規律
# 切記需要只留個位數去做計算，避免過多位數造成TLE
MAX = 100
table = [0] * (MAX+1)
for i in range(1, MAX+1):
    table[i] += (i**i + table[i-1]) % 10

while True:
    num = int(input())
    if num == 0:
        break
    
    print(table[num%100])
# 2026.05.24 二刷
