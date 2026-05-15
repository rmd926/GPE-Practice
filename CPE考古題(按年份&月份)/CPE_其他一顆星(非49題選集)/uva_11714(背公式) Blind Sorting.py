import math
while True:
    try:
        n = int(input())
    except:
        break
    
    ans = n + math.ceil(math.log2(n)) - 2
    print(ans)
