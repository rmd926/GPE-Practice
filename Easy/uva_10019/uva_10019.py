TC = int(input())
while True:
    try:
        N = int(input())
        hex_to_d = int(str(N), 16)

        bin_N = bin(N)[2:]
        hex_N = bin(hex_to_d)[2:]

        count_bin_N = 0
        count_hex_N = 0

        for i in bin_N:
            if i == '1':
                count_bin_N += int(i)
        
        for j in hex_N:
            if j == '1':
                count_hex_N += int(j)

        print(f"{count_bin_N} {count_hex_N}")
    except:
        break