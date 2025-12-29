'''
把數學式子列出來暴力解即可
'''
while True:
	try:
		cod = list(map(float, input().split()))
		if(cod[0] == cod[4] and cod[1] == cod[5]):
			x4 = cod[2] + cod[6] - cod[4]
			y4 = cod[3] + cod[7] - cod[5]
		elif(cod[0] == cod[6] and cod[1] == cod[7]):
			x4 = cod[2] + cod[4] - cod[0]
			y4 = cod[3] + cod[5] - cod[1]
		elif(cod[2] == cod[6] and cod[3] == cod[7]):
			x4 = cod[0] + cod[4] - cod[2]
			y4 = cod[1] + cod[5] - cod[3]
		elif(cod[2] == cod[4] and cod[3] == cod[5]):
			x4 = cod[0] + cod[6] - cod[2]
			y4 = cod[1] + cod[7] - cod[3]
			
		print(f"{x4:.3f} {y4:.3f}")
	except EOFError:
		break;
