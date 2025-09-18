TC = int(input())

for i in range(TC):
    best = -1
    lucky_site = []

    for _ in range(10):
        site, score = input().split()
        if int(score) > best: # update best value
            best = int(score)
            lucky_site = [site]

        elif int(score) == best: # same score -> show all sites
            lucky_site.append(site)

    print(f"Case #{i+1}:")
    print("\n".join(lucky_site))