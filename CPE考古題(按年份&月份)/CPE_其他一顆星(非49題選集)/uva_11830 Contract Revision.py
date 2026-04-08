while True:
    try:
        D, N = map(int, input().split())
    except:
        break

    if D == N == 0:
        break   
    output = ""

    for char in str(N):
        if char == str(D):
            continue
        else:
            output += char
            
    if output == "": # 會有完全顯示不出來的case -> 0
        print(0)
    else: # 轉成int避免出現0開頭或是全0的case
        print(int(output))
