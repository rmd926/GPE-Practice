# https://zerojudge.tw/ShowProblem?problemid=c291

n = int(input())
friends_list = [int(x) for x in input().split()]
visit_status = [False] * n

count = 0

for i in range(n):
    if visit_status[i] == True:
        continue
    else:
        visit_status[i] = True
        pair_num = friends_list[i]
        count += 1

    while pair_num != i: # 只要i配到的數字還不是等於起頭的那個i的話
        visit_status[pair_num] = True
        pair_num = friends_list[pair_num] # 再把i配到的那個數字更新成那個數字該對應的數字

print(count)
