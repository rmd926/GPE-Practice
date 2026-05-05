MAX = 100

male = [0] * (MAX+1)
female = [0] * (MAX+1)

male[0] = 0
female[0] = 1

for i in range(1, MAX+1):
    male[i] = male[i-1] + female[i-1]
    female[i] = male[i-1] + 1

while True:
    try:
        n = int(input())
    except:
        break
    if n == -1:
        break
    
    print(f"{male[n]} {male[n] + female[n]}")
