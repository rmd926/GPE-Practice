tc = int(input())
for t in range(tc):
    try:
        target = input()
    except:
        break

    ans = 0
    for char in target:
        if char in "adgjmptw":
            ans += 1

        elif char in "behknqux":
            ans += 2

        elif char in "cfilorvy":
            ans += 3

        elif char in "sz":
            ans += 4

        else:
            ans += 1
                
    print(f"Case #{t+1}: {ans}")
