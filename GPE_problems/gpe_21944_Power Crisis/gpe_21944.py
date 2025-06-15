def find_min_m(N):
    m = 1
    while True:
        regions = list(range(1,N+1))
        regions.pop(0)
        idx = 0
        while len(regions) > 1:
            idx = (idx+m-1) % len(regions)
            regions.pop(idx)
        if regions[0] == 13:
            return m
        m += 1

def main():
    N = int(input())
    while N != 0:
        print(find_min_m(N))
        N = int(input())

if __name__ == '__main__':
    main()