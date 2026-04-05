def is_prime(target: int):
    if target <= 2:
        return True # 1 is prime in this question
    
    for i in range(2, int(target**0.5)+1):
        if target % i == 0:
            return False
        
    return True

while True:
    try:
        target = input()
    except:
        break
    
    temp = 0
    for char in target:
        if "A" <= char <= "Z":
            temp += (ord(char) - 38)

        elif "a" <= char <= "z":
            temp += (ord(char) - 96)
    
    if is_prime(temp):
        print("It is a prime word.")
        
    else:
        print("It is not a prime word.")
