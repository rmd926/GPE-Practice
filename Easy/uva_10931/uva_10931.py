while True:
    target = int(input())
    if target == 0:
        break
    
    count = 0
    bin_target = bin(target)[2:]

    for i in str(bin_target):
        if i == '1':
            count += int(i)
    print(f"The parity of {bin_target} is {count} (mod 2).")
