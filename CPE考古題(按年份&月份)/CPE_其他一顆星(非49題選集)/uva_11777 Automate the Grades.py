tc = int(input())
for t in range(tc):
    try:
        target = list(map(int, input().split()))
    except:
        break
    
    score = 0
    temp = []
    for i in range(4):
        score += target[i]
    
    for j in range(4, 7):
        temp.append(target[j])
    
    temp = sorted(temp)[1:]
    score += sum(temp) / 2

    if score >= 90:
        print(f"Case {t+1}: A")

    elif 90 > score >= 80:
        print(f"Case {t+1}: B")

    elif 80 > score >= 70:
        print(f"Case {t+1}: C")

    elif 70 > score >= 60:
        print(f"Case {t+1}: D")
        
    else:
        print(f"Case {t+1}: F")
