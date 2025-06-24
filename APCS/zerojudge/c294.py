# https://zerojudge.tw/ShowProblem?problemid=c294

a = [int(i) for i in input().split()]

a.sort()
print(*a)

if a[0]+a[1] <= a[2]:
    print('No')
elif a[0]**2 + a[1]**2 == a[2]**2:
    print('Right')
elif a[0]**2 + a[1]**2 > a[2]**2:
    print('Acute')
else:
    print('Obtuse')
