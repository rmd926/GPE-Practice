# case = 0
# while True:
#     try:
#         s = input().strip()
#     except EOFError:
#         break

#     case += 1
#     print(f"Case {case}:")
#     tc = int(input())

#     for _ in range(tc):
#         i, j = map(int, input().split())
#         # if i == 0 and j == 0:
#         #     break
#         if (
#             sum(int(num) for num in s[min(i, j):max(i, j) + 1]) == max(i, j) - min(i, j) + 1
#             or sum(int(num) for num in s[min(i, j):max(i, j) + 1]) == 0
#         ):
#             print('Yes')
#         else:
#             print('No')
# TLE lol so do not use sum!!!


case = 0
while True:
    try:
        s = input().strip()
    except EOFError:
        break

    case += 1
    print(f"Case {case}:")
    tc = int(input())

    for _ in range(tc):
        i, j = map(int, input().split())
        # if i == 0 and j == 0:
        #     break
        if (
            s[min(i, j):max(i, j) + 1].count('1') == max(i, j) - min(i, j) + 1
            or s[min(i, j):max(i, j) + 1].count('0') == max(i, j) - min(i, j) + 1
        ):
            print('Yes')
        else:
            print('No')
