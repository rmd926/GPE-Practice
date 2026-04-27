tc = 1
while True:
    try:
        target = input()
    except:
        break

    if target == "0":
        break
    
    if tc > 1:
        print()

    print(f"Original number was {target}")
    cur = []
    count = 1
    temp = 0
  
    while True:
        max_num = "".join(sorted(target)[::-1])
        min_num = "".join(sorted(target))
        temp = int(max_num) - int(min_num)
        print(f"{int(max_num)} - {int(min_num)} = {temp}")

        target = str(temp)
        if temp not in cur:
            cur.append(temp)
            count += 1
        else:
            break
    
    print(f"Chain length {count}")
    tc += 1
