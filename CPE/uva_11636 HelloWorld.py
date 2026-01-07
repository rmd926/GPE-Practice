'''
起始從只有1行開始，複製完變成2、4、8、16... 因為如果target是30，他可以複製非2^n倍數的補到30
所以直接用一個while loop判斷目標值是否大於當前行數，並且搭配計數即可。
'''

tc = 1
while True:
    target = int(input())
    if target == -1:
        break
    
    temp = 1 
    count = 0

    while target > temp:
        temp *= 2
        count += 1
    print(f"Case {tc}: {count}")

    tc += 1