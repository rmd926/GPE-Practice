while True:
	bulb_num = int(input())
	if bulb_num == 0:
		break
	else:
		if int(bulb_num ** 0.5) ** 2 == bulb_num:
			print("yes")
		else:
			print("no") 