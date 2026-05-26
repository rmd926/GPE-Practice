case = 1

while True:
    s = input()

    if s == "end":
        break

    stack = []

    for ch in s:
        status = False

        for i in range(len(stack)):
            if stack[i] >= ch:
                stack[i] = ch
                status = True
                break

        if status == False:
            stack.append(ch)

    print(f"Case {case}: {len(stack)}")
    case += 1

# 花了2 hrs 結果完全會錯意 完全法克
