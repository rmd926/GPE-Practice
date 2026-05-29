# v1
import sys

while True:
    line = sys.stdin.readline()

    if line == "":
        break

    M, N = map(int, line.split())

    last_sum = sum(map(int, sys.stdin.readline().split()))

    for _ in range(M - 1):
        cur_sum = sum(map(int, sys.stdin.readline().split()))

        print(last_sum - cur_sum)

        last_sum = cur_sum

# v2
while True:
    try:
        M, N = map(int, input().split())
    except:
        break

    last_sum = sum(map(int, input().split()))

    for _ in range(M - 1):
        cur_sum = sum(map(int, input().split()))

        print(last_sum - cur_sum)

        last_sum = cur_sum
