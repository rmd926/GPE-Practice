keyboard = "`1234567890-=QWERTYUIOP[]\\ASDFGHJKL;'ZXCVBNM,./"

while True:
    target = input()
    
    for char in target:
        if char == " ":
            print(" ", end="")
        else:
            print(keyboard[keyboard.index(char) - 1], end="")
    print()