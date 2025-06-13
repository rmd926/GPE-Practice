TC = int(input())

months_days = [0,31,28,31,30,31,30,31,31,30,31,30,31]
day_type = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

for i in range(TC):
    temp = 0
    month, date = map(int,input().split())

    for j in range(month):
        temp += months_days[j]
    print(day_type[(temp+date+4) % 7]) # +4 cause 1/1 is Friday => last year 12/31 is Thursday