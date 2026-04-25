while True:
    try:
        s, t = map(str, input().split())
    except:
        break

    ptr_s, ptr_t = 0, 0
    while ptr_s < len(s) and ptr_t < len(t):
        if s[ptr_s] == t[ptr_t]:
            ptr_s += 1
            ptr_t += 1
        else:
            ptr_t += 1
    
    if ptr_s == len(s):
        print("Yes")
    else:
        print("No")
