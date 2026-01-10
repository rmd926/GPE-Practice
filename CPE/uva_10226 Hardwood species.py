tc = int(input())

# 吃掉 tc 後面那行空白（有些測資可能不只一行空白）
while True:
    try:
        line = input()
    except EOFError:
        line = ""
        break
    if line == "":
        break

for i in range(tc):
    total = 0
    dict = {}

    # ---- 先讀到本 case 的第一個非空白行（避免多空白行導致 total=0）----
    while True:
        try:
            target = input()
        except EOFError:
            target = ""  # 視為結束
            break
        if target != "":
            break

    # 如果真的讀不到任何資料（EOF），就直接結束
    if target == "":
        break

    # 把第一行先納入統計
    if target not in dict:
        dict[target] = 1
    else:
        dict[target] += 1
    total += 1

    # ---- 繼續讀本 case 直到空白行或 EOF ----
    while True:
        try:
            target = input()
        except EOFError:
            target = ""
        if target == "":
            break
        if target not in dict:
            dict[target] = 1
        else:
            dict[target] += 1
        total += 1

    # ---- 輸出：依 key 排序，百分比到小數點後 4 位 ----
    for key, value in sorted(dict.items()):
        print(f"{key} {100.0 * value / total:.4f}")

    # 測資之間空一行（最後一筆不印）
    if i != tc - 1:
        print()
