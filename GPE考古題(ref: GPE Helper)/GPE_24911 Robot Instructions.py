tc = int(input())
for _ in range(tc):
    try:
        n = int(input())
    except:
        break
    pos = 0
    record = []

    for _ in range(n):
        try:
            command = input()
        except:
            break
        
        if command == "LEFT":
            pos -= 1
            record.append(command)
          
        elif command == "RIGHT":
            pos += 1
            record.append(command)
          
        else:
            index = command.split()[-1]
            index = int(index)
          
            if record[index-1] == "LEFT":
                pos -= 1
                record.append("LEFT")
              
            elif record[index-1] == "RIGHT":
                pos += 1
                record.append("RIGHT")
        
    print(pos)
