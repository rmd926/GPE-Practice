while True:
    try:
        J, R = map(int, input().split())
    except:
        break

    if J == R == 0:
        break

    score = [0] * J
    target = list(map(int, input().split()))

    for i in range(len(target)):
        score[i % J] += target[i]
    
    max_score = max(score)
    winner = 0

    for i in range(len(score)):
        if score[i] == max_score:
            winner = i + 1
            break
    
    print(winner)
