TC = int(input())
temp = {} # dict to save {country: times}

for i in range(TC):
    target = input().split()
    country = target[0]

    if country not in temp:
        temp[country] = 1
    else:
        temp[country] += 1
    
for country in sorted(temp):
    print(country, temp[country])