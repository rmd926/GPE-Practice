N = int(input())
for _ in range(N):
	target = input()
	while "()" in target or "[]" in target:
		target = target.replace("()","").replace("[]","")
		
	if len(target) > 0:
		print("No")
		
	else:
		print("Yes")