tc = int(input())
for t in range(tc):
    try:
        output = input()
        gt = input()
    except:
        break

    if output == gt:
        print(f"Case {t+1}: Yes")

    elif output.replace(" ", "") == gt or gt.replace(" ", "") == output:
        print(f"Case {t+1}: Output Format Error")
    
    else:
        print(f"Case {t+1}: Wrong Answer")
