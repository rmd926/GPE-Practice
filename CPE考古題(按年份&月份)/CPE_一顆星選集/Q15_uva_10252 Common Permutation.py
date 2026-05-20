while True:
    try:
        s1 = input()
        s2 = input()
    except:
        break

    ans = ""
    for ch in "abcdefghijklmnopqrstuvwxyz":
        count = min(s1.count(ch), s2.count(ch))
        ans += ch * count

    print(ans)
# 2026.05.20 二刷 要留意多次數的字母，而不是直接取set
