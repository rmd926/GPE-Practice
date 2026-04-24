tc = int(input())
for t in range(tc):
    ws, we = input().split()
    ms, me = input().split()
    
    # 轉成分鐘方便比較
    ws = int(ws[:2]) * 60 + int(ws[3:])
    we = int(we[:2]) * 60 + int(we[3:])
    ms = int(ms[:2]) * 60 + int(ms[3:])
    me = int(me[:2]) * 60 + int(me[3:])
    
    # 不重疊：會議在妻子時間之前結束，或之後開始
    if me < ws or ms > we:
        print(f"Case {t+1}: Hits Meeting")
    else:
        print(f"Case {t+1}: Mrs Meeting")
