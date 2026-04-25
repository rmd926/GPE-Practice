while True:
    try:
        G, target = map(str, input().split())
    except:
        break
    
    if G == "0":
        break

    G = int(G)
    n = len(target) // G

    ans = ""
    for i in range(0, len(target), n):
        ans += target[i: i+n][::-1]
    
    print(ans)
