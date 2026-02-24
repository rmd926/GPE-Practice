temp = []
while True:
	target = int(input())
	temp.append(target)
	temp = sorted(temp)
	
	if len(temp) % 2 == 0:
		print((temp[len(temp)//2] + temp[len(temp)//2-1])//2)
	else:
		print(temp[len(temp)//2])
