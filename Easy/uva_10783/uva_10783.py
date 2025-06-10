TC = int(input())

for i in range(TC):
    a = int(input()) # lower bound
    b = int(input()) # upper bound

    ans = 0
    pointer = 0

    if a % 2 == 0: # a is an even num.
        pointer = a + 1
    else:
        pointer = a
    
    for odd in range(pointer, b+1, 2):
        ans += odd
    
    print(f"Case {i+1}: {ans}")
