tc = int(input())
for _ in range(tc):
	target = input() # 先用input()，若先轉int的話會有部分測資過不了= =
	seq = list(map(int, input().split()))
	status = True
	
	for num in seq[1:]:
		if int(target) % num != 0:
			status = False
			break
		else:
			continue
	
	if status:
		print(f"{target} - Wonderful.")
	else:
		print(f"{target} - Simple.")
			
