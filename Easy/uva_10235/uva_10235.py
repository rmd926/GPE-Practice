def prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def Solution(n):
    if prime(n) and prime(int(str(n)[::-1])) and n != int(str(n)[::-1]):
        return f"{n} is emirp."
    elif prime(n):
        return f"{n} is prime."
    else:
        return f"{n} is not prime."

while True:
    try:   
        n = int(input())
        print(Solution(n))
    except:
        break