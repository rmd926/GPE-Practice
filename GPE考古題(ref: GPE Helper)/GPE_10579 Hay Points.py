lookup = {}
while True:
    try:
        m, n = map(int, input().split())
    except:
        break
    
    for _ in range(m):
        word, value = map(str, input().split())
        lookup[word] = int(value)
    
    for _ in range(n):
        ans = 0
        while True:
            try:
                article = input()
            except:
                break

            if article == ".":
                break
            
            for word in article.split():
                if word in lookup:
                    ans += lookup[word]
            
        print(ans)
