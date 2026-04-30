while True:
    try:
        year = int(input())
    except:
        break

    leap = False
    # 判斷閏年
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print("This is leap year.")
        leap = True

    # huluculu festival year
    if year % 15 == 0:
        print("This is huluculu festival year.")

    # bulukulu festival year (只有閏年才判斷)
    if leap and year % 55 == 0:
        print("This is bulukulu festival year.")

    # ordinary year
    if not leap and year % 15 != 0:
        print("This is an ordinary year.")

    print()  # 題目要求每組輸出後要空一行
