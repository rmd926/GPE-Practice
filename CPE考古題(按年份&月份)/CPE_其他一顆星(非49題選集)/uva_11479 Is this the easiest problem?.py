tc = int(input())
for t in range(tc):
    target = list(map(int, input().split()))
    target.sort()

    if target[0] + target[1] <= target[2]:
        print(f"Case {t+1}: Invalid")
    
    else:
        if len(set(target)) == 1:
            print(f"Case {t+1}: Equilateral")
        
        elif len(set(target)) == 2:
            print(f"Case {t+1}: Isosceles")
        
        else:
            print(f"Case {t+1}: Scalene")
