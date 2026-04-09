target = [1]

p2, p3, p5 = 0, 0, 0

while len(target) < 1500:
    num2 = target[p2] * 2
    num3 = target[p3] * 3
    num5 = target[p5] * 5

    temp = min(num2, num3, num5)
    target.append(temp)

    if temp == num2:
        p2 += 1
    
    if temp == num3:
        p3 += 1
    
    if temp == num5:
        p5 += 1

print(f"The 1500'th ugly number is {target[-1]}.")
