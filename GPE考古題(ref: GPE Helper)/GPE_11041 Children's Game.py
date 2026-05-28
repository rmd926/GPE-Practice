while True:
    try:
        n = int(input())
    except:
        break
    if n == 0:
        break

    seq = list(map(str, input().split()))
    for i in range(n):
        for j in range(i+1, n):
            if int(seq[i] + seq[j]) < int(seq[j]+seq[i]):
                seq[i], seq[j] = seq[j], seq[i]

    print("".join(seq))
