while True:
	A, B = map(int, input().split())
	if A == 0 and B == 0:
		break
	
	card_A = list(map(int, input().split()))
	card_B = list(map(int, input().split()))
	
	rest_A = sorted(list(set(card_A) - set(card_B)))
	rest_B = sorted(list(set(card_B) - set(card_A)))
	
	print(min(len(rest_A), len(rest_B)))
	