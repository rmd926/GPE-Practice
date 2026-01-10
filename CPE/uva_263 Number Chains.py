'''
1) 先輸出原始數字。
2) 重複執行以下步驟：
   - 將數字的各位數字由大到小排序組成 a
   - 將數字的各位數字由小到大排序組成 b
   - 計算 ans = a - b
   - 印出運算過程：a - b = ans
   - 將 target 更新為 ans
   - 若 target 曾經出現過，代表進入循環，停止
3) 最後輸出鏈的長度（總共做了幾次相減），並印出空白行分隔下一筆輸入。
'''

while True:
	target = input()
	if target == "0":
		break
	print(f"Original number was {target}")
	
	temp = list()
	count = 0
	
	while target not in temp:
		a = "".join(sorted(target)[::-1])
		b = "".join(sorted(target))
		temp.append(target)
		
		target = str(int(a) - int(b))
		print(f"{int(a)} - {int(b)} = {target}")
		count += 1
	print(f"Chain length {count}")
	print()