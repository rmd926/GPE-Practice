T = int(input())

for _ in range(T):
    n = int(input())
    pos = 0
    history = []  # 存 'LEFT' / 'RIGHT'

    for _ in range(n):
        move = input()
        if move == 'LEFT':
            pos -= 1
            history.append(move)

        elif move == 'RIGHT':
            pos += 1
            history.append(move)

        else:  # SAME AS X
            i = int(move.split()[-1])
            lookup = history[i - 1]
            if lookup == 'LEFT':
                pos -= 1
            else:
                pos += 1
            history.append(lookup)
        
    print(pos)
