while True:
    try:
        N, M = map(int, input().split())
    except:
        break
    
    lookup = {}
    for _ in range(N):
        single, multi = map(str, input().split())
        lookup[single] = multi
    
    for _ in range(M):
        target = input()
        if target in lookup:
            print(lookup[target])
        else:
            if target[-1] in "osx" or target[-2:] == "ch" or target[-2:] == "sh":
                print(target+"es")
            
            elif target[-2] not in "aeiou" and target[-1] == "y":
                print(target[:-1]+"ies")
            
            else:
                print(target+"s")
