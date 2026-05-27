while True:
    try:
        n = int(input())
    except:
        break

    if n == 0:
        break
    root = int(n**0.5)
  
    if root ** 2 == n:
        print("yes")
    else:
        print("no")
