mirror_mapping = {
    'A': 'A', 'E': '3', '3': 'E',
    'H': 'H', 'I': 'I', 'J': 'L', 'L': 'J',
    'M': 'M', 'O': 'O', 'S': '2', '2': 'S',
    'T': 'T', 'U': 'U', 'V': 'V', 'W': 'W',
    'X': 'X', 'Y': 'Y', 'Z': '5', '5': 'Z',
    '1': '1', '8': '8'
} # 這邊放會有mirror的

while True:
    try:
        target = input()
    except:
        break

    palindrome = True
    mirror = True

    if target != target[::-1]:
        palindrome = False
    
    for i in range(len(target)):
        if target[i] not in mirror_mapping or mirror_mapping[target[i]] != target[len(target)-i-1]:
            mirror = False
        
    if palindrome and mirror:
        print(f"{target} -- is a mirrored palindrome.")

    elif palindrome and not mirror:
        print(f"{target} -- is a regular palindrome.")
    
    elif not palindrome and mirror:
        print(f"{target} -- is a mirrored string.")
    
    elif not palindrome and not mirror:
        print(f"{target} -- is not a palindrome.")
    
    print()
