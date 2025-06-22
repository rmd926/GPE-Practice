TC = int(input())

for i in range(TC):
    x = int(input(),2)
    y = int(input(),2)

    while y > 0:
        x, y = y, x % y
    if x > 1:
        print(f"Pair #{i+1}: All you need is love!")
    else:
        print(f"Pair #{i+1}: Love is not all you need!")
