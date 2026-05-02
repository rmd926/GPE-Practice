tc = int(input())
for t in range(tc):
    try:
        n = int(input())
    except:
        break
    ans = []

    for i in range(2, n+1):
        if n % i == 0:
            ans.append(i)
            ans.append(n//i)
            
            if len(ans) == 4:
                break
    
    print(f"Case #{t+1}: {n} = {ans[0]} * {ans[1]} = {ans[2]} * {ans[3]}")
