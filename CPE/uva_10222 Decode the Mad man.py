
keyboard = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./"
tc = int(input())

for _ in range(tc):
    target = input()
    
    for char in target.lower():
        if char == " ":
            print(" ", end="")
        else:
            print(keyboard[keyboard.index(char) - 2], end="")
    print()