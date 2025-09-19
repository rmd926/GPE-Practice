# GPE 11006 - Rank the Languages（外牆 + 走過設為牆的寫法）

TC = int(input())
for tc in range(TC):
    row, col = map(int, input().split())
    inner = [list(input().strip()) for _ in range(row)]

    WALL = '*'
    MAP = [[WALL] * (col + 2)] + [[WALL] + r + [WALL] for r in inner] + [[WALL] * (col + 2)]

    cnt = {} # dictionary
    for i in range(1, row + 1):
        for j in range(1, col + 1):
            if 'a' <= MAP[i][j] <= 'z': # 判斷是否是小寫字母
                ch = MAP[i][j]
                if ch in cnt: # 如果有在連通塊的dictionary出現過直接加一
                    cnt[ch] += 1
                else:
                    cnt[ch] = 1
                
                start = (i,j)
                stack = [start]
                MAP[i][j] = WALL # visited 把改點改寫成和外牆一樣

                while stack: 
                    x, y = stack.pop() # 把當前stack的x, y pop出來並且去搜以下四個if是否有符合並且push進去這個stack
                    if MAP[x + 1][y] == ch:
                        MAP[x + 1][y] = WALL
                        stack.append((x + 1, y))

                    if MAP[x - 1][y] == ch:
                        MAP[x - 1][y] = WALL
                        stack.append((x - 1, y))

                    if MAP[x][y + 1] == ch:
                        MAP[x][y + 1] = WALL
                        stack.append((x, y + 1))

                    if MAP[x][y - 1] == ch:
                        MAP[x][y - 1] = WALL
                        stack.append((x, y - 1))

    print(f"World #{tc + 1}")
    for ch in sorted(cnt, key=lambda c: (-cnt[c], c)):
        print(f"{ch}: {cnt[ch]}")
