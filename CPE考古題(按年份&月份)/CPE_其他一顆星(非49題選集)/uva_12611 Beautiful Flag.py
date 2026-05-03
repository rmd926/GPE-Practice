tc = int(input())
for t in range(tc):
    try:
        r = int(input())
    except:
        break

    print(f"Case {t+1}:")
    X = 5 * r
    Y = 3 * r
    
    print(f"{int(-0.45 * X)} {int(0.5*Y)}")
    print(f"{int(0.55 * X)} {int(0.5*Y)}")
    print(f"{int(0.55 * X)} {int(-0.5*Y)}")
    print(f"{int(-0.45 * X)} {int(-0.5*Y)}")
