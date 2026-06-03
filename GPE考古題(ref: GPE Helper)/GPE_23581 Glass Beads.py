tc = int(input())
for _ in range(tc):
    try:
        target = input()
    except:
        break

    compare = []
    for i in range(len(target)):
        temp = target[(i+1) % len(target):] + target[:(i+1) % len(target)]
        compare.append(temp)
    
    min_ans = min(compare)
    for word in compare:
        if word == min_ans:
            print(compare.index(word) + 2)
            break
