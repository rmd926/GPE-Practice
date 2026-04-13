MAX = 1000000
is_prime = [True] * (MAX+1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(MAX**0.5)+1):
    if is_prime[i]:
        for j in range(i**2, MAX+1, i):
            is_prime[j] = False

p_list = []
for p in range(2, MAX+1):
    if is_prime[p]:
        p_list.append(p)

while True:
    try:
        n = int(input())
    except:
        break
    if n == 0:
        break

    temp = set()
    
    for num in p_list:
        if n % num == 0:
            temp.add(num)
        
    print(f"{n} : {len(temp)}")
