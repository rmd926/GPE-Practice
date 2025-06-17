MAX = 600
def main():
    global MAX
    fact = [1] * (MAX+1)
    for i in range(1, MAX+1):
        fact[i] *= fact[i-1] * i

    while True:
        line = input().strip()
        if not line:
            continue
        n = int(line)
        if n == 0:
            break

        trees = fact[2*n] // (fact[n] * (n+1))
        print(trees)

if __name__ == "__main__":
    main()