while True:
    target = input()
    # chr(): 輸入一個整數，回傳他的ascii
    # ord(): 輸入一個ascii，回傳一個整數
    for char in target:
        print(chr(ord(char)-7),end="")
    print()