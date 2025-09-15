# n = int(input())
# # self_list = [int(x) for x in range(0, n, 1)]

# friends_list = [int(i) for i in input().split()]
# visit_flag = [False] * n # record the status of visit
# count = 0

# for i in range(n):
#     if visit_flag[i] == True: # continue
#         continue
#     else: #doesn't visit yet
#         visit_flag[i] = True
#         pointer = friends_list[i]
#         count += 1
#     while pointer != i: #只要指標還不是指到該群組的first num
#         visit_flag[pointer] = True
#         pointer = friends_list[pointer] #pointer繼續更新成friends_list對應到的數字

# print(count)











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












