tc = int(input())
for _ in range(tc):
    a, b = map(int, input().split())
    temp = []
    for _ in range(a):
    	dna = input()
    	temp.append(dna)
    
    output = ""
    for j in range(b):  
        lookup = {}
        for i in range(a):  
            ch = temp[i][j]
            if ch not in lookup:
                lookup[ch] = 1
            else:
                lookup[ch] += 1

        max_count = max(lookup.values())
        candidates = []
        
        for key, value in sorted(lookup.items()):
            if value == max_count:
                candidates.append(key)

        output += min(candidates)
    
    error = 0
    for dna in temp:
        for i in range(b):
            if dna[i] != output[i]:
                error += 1
    
    print(output)
    print(error)
