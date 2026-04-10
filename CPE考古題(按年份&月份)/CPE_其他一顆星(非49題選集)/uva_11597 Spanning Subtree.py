# k * (k-1) / 2 = n
# -1 +- sqrt(1+4k) / 2
tc = 1
while True:
    try:
        n = int(input())
    except:
        break

    if n == 0:
        break
    
    print(f"Case {tc}: {n//2}")
    tc += 1
