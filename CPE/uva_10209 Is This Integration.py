import math

pi = math.pi
while True:
	try:
		a = float(input())
	except EOFError:
		break
	
	z = a*a - a*a*pi/4
	z -= a*a*pi/4 - a*a*pi/6 - ( a*a*pi/6 - a*a*(3**0.5)/4 )
	y = a*a - a*a*pi/4 - 2*z
	x = a*a - 4*y - 4*z
	print("{:.3f} {:.3f} {:.3f}".format(x, 4*y ,4*z))
