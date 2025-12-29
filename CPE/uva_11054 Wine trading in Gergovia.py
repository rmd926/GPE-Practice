'''
解題流程：
- current 表示目前累積和（從第一個數開始）。
- 每走到下一個數之前，先把當前 |current| 加進 ans。
- 再把下一個數加到 now 更新累積和。
- 全部處理完印出 ans。
'''

while True:
    num = int(input())
    if num == 0:
        break

    target = list(map(int, input().split()))
    current = target[0]
    ans = 0
    
    for i in range(1, num):
       ans += abs(current)
       current += target[i]

    print(ans) 