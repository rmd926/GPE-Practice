tc = int(input())

notes = {
    'c': "0111001111",
    'd': "0111001110",
    'e': "0111001100",
    'f': "0111001000",
    'g': "0111000000",
    'a': "0110000000",
    'b': "0100000000",
    'C': "0010000000",
    'D': "1111001110",
    'E': "1111001100",
    'F': "1111001000",
    'G': "1111000000",
    'A': "1110000000",
    'B': "1100000000"
}

for _ in range(tc):
	target = input()
	prev = "0000000000"
	ans = [0] * 10
	
	for char in target:
		cur = notes[char]
		for i in range(10):
			if prev[i] == "0" and cur[i] == "1":
				ans[i] += 1		
		prev = cur
	
	print(*ans)
