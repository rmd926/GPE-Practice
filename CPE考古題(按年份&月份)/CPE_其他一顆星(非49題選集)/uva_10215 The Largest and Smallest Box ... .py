while True:
    try:
        L, W = map(eval, input().split())
    except:
        break
    
    x_max = ((L+W) - (L**2 - L*W + W**2) ** 0.5) / 6
    x_min = min(L, W) / 2

    print(f"{x_max + 1e-9:.3f} 0.000 {x_min + 1e-9:.3f}")
