import sys
while True:
	n = int(sys.stdin())
	if n == 0:
		break
	else:
		if n % 17 == 0:
			print('1')
		else:
			print('0')