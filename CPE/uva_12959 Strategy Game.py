while True:
    J, R = map(int, input().split())
    if J == 0 and R == 0:
        break
    target = list(map(int, input().split()))

    players = [0] * J
    max_score = 0
    winner = 0

    for index, score in enumerate(target):
        players_index = index % J
        players[players_index] += score

        if players[players_index] >= max_score:
            max_score = players[players_index]
            winner = players_index + 1
    print(winner)