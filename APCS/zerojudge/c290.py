while True:
    try:
        num = int(input())

        odd = 0
        even = 0

        for i in range(0, len(str(num)), 2):
            odd += int(str(num)[i])
        for j in range(1, len(str(num)), 2):
            even += int(str(num)[j])

        print(abs(odd-even))
    except:
        break