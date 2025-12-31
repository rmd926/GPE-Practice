def isPrime(num):
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def output(num):
    if isPrime(num) and isPrime(int(str(num)[::-1])) and num != int(str(num)[::-1]):
        return f"{num} is emirp."
    elif isPrime(num):
        return f"{num} is prime."
    else:
        return f"{num} is not prime."

while True:
    target = int(input())
    print(output(target))
