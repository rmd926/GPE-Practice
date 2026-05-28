tc = 1
while True:
    try:
        target = input()
    except:
        break
    
    print(f"Case {tc}:")
    prefix = [0] * (len(target)+1)
    for i in range(len(target)):
        prefix[i+1] = prefix[i] + int(target[i])
    
    n = int(input())
    for _ in range(n):
        low, high = map(int, input().split())
        if low > high:
            low, high = high, low
        
        temp = prefix[high + 1] - prefix[low]
        if temp == 0 or temp == high - low + 1:
            print("Yes")
        else:
            print("No")

    tc += 1
# 這題不能用原本方式，在UVA online judge上面會TLE，必須要用prefix sum
