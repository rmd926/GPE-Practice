while True:
	num, target = map(str, input().split())
	if num == "0":
		break
	
	group_len = len(target) // int(num)
	output = ""
	for i in range(0, len(target), group_len):
		output += (target[i: group_len+i][::-1])
		
	print("".join(output))
