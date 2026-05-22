while True:
	target = input()
	if target == "0":
		break
	elif target == "9":
		print("9 is a multiple of 9 and has 9-degree 1.")
	
	elif int(target) % 9 == 0:
		cur_num = target
		count = 0
		
		while int(cur_num) != 9:
			count += 1
			temp = 0
			for ch in cur_num:
				temp += int(ch)
			cur_num = str(temp)
		print(f"{target} is a multiple of 9 and has 9-degree {count}.")
	
	else:
		print(f"{target} is not a multiple of 9.")

# 2026.05.22 二刷 要注意% 9那邊 count怎麼加
