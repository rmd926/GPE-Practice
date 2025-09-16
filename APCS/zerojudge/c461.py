
'''
case:
a = 0; b = 0
a = 0; b != 0
a != 0; b = 0
a != 0; b != 0   
各個branch 搭配c = 0、c != 0
''' 
# https://zerojudge.tw/ShowProblem?problemid=m931
a,b,c = map(int,input().split())

if a == 0 and b == 0:
    if c == 0:
        print("AND\nOR\nXOR")
    elif c == 1:
        print("IMPOSSIBLE")

elif a == 0 and b != 0:
    if c == 0:
        print("AND")
    elif c == 1:
        print("OR\nXOR")

elif a != 0 and b == 0:
    if c == 0:
        print("AND")
    elif c == 1:
        print("OR\nXOR")

elif a != 0 and b != 0:
    if c == 0:
        print("XOR")
    elif c == 1:
        print("AND\nOR")