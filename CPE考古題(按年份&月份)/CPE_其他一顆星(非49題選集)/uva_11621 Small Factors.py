record = []
MAX = 2 ** 31

num = 1
while num <= MAX:
    temp = num
    while temp <= MAX:
        record.append(temp)
        temp *= 3
    num *= 2

record.sort()

while True:
    target = int(input())

    if target == 0:
        break

    for num in record:
        if num >= target:
            print(num)
            break
