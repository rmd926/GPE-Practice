import sys

current = []
ans = set()

for line in sys.stdin:
	for char in line:
		if "A" <= char <= "Z" or "a" <= char <= "z":
			current.append(char.lower())
		else: # 如果遇到非字母，且current這個list存在時，先把current的元素加到ans內，然後清空
			if current:
				ans.add("".join(current))
				current = []

if current:
	ans.add("".join(current))
	
for word in sorted(ans):	
	print(word)
