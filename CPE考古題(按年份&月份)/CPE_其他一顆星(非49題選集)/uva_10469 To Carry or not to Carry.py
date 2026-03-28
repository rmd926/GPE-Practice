# 二進制XOR就解出來了
while True:
    try:
        a, b = map(int, input().split())
        print(a ^ b)
    except EOFError:
        break
