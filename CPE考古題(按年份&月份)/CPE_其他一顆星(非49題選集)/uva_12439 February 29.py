month_num = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

def leap_count(year):
    return year // 4 - year // 100 + year // 400

tc = int(input())
for t in range(tc):
    m1, d1, y1 = map(str, input().split())
    m2, d2, y2 = map(str, input().split())

    d1 = int(d1[:-1])
    d2 = int(d2[:-1])
    y1 = int(y1)
    y2 = int(y2)

    if month_num[m1] > 2:
        y1 += 1
    
    if month_num[m2] < 2 or (month_num[m2] == 2 and d2 < 29):
        y2 -= 1

    ans = leap_count(y2) - leap_count(y1-1)
    print(f"Case {t+1}: {ans}")
