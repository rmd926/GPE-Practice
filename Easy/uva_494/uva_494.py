import sys
'''
逐行讀到 EOF。

掃每個字元，維護 flag 表示是否在單字內。

若 ch.isalpha() 且 flag=False，開啟新單字：count+=1; flag=True。

若遇非字母，單字結束：flag=False。

行末輸出 count。
'''
for line in sys.stdin:
	count = 0
	flag = False #如果是word的話，改True
	
	for char in line:
		if char.isalpha():
			if not flag:
				count += 1
				flag = True
		else:
			flag = False
	print(count)
	
'''
while True:
    try:
        line = input()
        count = 0
        flag = False

        for char in line:
            if char.isalpha():
                if not flag:
                    count += 1
                    flag = True
            else:
                flag = False
        print(count) 
    except:
          break
'''	

    
