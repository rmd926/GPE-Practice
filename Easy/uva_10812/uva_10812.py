TC = int(input())

for i in range(TC):
    ab_sum, ab_diff = map(int,input().split())

    if ab_sum < ab_diff or (ab_sum+ab_diff) % 2 != 0:
        print('impossible')
    else:
        print((ab_sum+ab_diff)//2, (ab_sum-ab_diff)//2)