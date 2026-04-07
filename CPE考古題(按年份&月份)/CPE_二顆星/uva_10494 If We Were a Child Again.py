while True:
    try:
        m, op, n = map(str, input().split())
    except:
        break
    
    if op == "/":
        print(int(m) // int(n))
        
    elif op == "%":
        print(int(m) % int(n))
