seq = []
while True:
	target = int(input())
	seq.append(target)
	seq = sorted(seq) # using sorted function to make this seq to be sorted => find median
	length = len(seq)
    
	if length % 2 == 0:
		print((seq[length//2] + seq[length//2-1]) // 2)
	else:
		print(seq[length//2])
	