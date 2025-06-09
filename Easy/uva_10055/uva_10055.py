while True:
    try:
        our, enemy = list(map(int, input().split()))
        print(abs(our-enemy))
    except:
        break
