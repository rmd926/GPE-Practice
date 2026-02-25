while True:
	H, U, D, F = map(int, input().split())
	if H == 0:
		break
	e =  U * (F / 100)
	day = 0
	climb = 0
	
	while True:
		day += 1
		climb += U
		
		if climb > H:
			print(f"success on day {day}")
			break
			
		climb -= D # slide down
		
		if climb < 0:
			print(f"failure on day {day}")
			break
			
		U = max(U-e, 0) # update the new U
