keyboard = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./"

while True:
	target = input()
	ans = ""
	
	for ch in target.lower():
		if ch in keyboard:
			ans += keyboard[keyboard.index(ch)-2]
		else:
			ans += ch
	print(ans)
# 2026.05.20 二刷
