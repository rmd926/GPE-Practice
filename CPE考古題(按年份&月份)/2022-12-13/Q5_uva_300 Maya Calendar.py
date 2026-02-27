haab = ['pop', 'no','zip', 'zotz', 'tzec', 'xul', 'yoxkin', 'mol', 'chen', 'yax',
        'zac', 'ceh', 'mac', 'kankin', 'muan', 'pax', 'koyab', 'cumhu', 'uayet']
        
tzolkin = ['imix', 'ik', 'akbal', 'kan', 'chicchan', 'cimi', 'manik', 'lamat', 'muluk',
           'ok', 'chuen', 'eb', 'ben', 'ix', 'mem', 'cib', 'caban', 'eznab', 'canac', 'ahau']
                    
tc = int(input())
print(tc)

for _ in range(tc):
    target = list(input().split())
    day, month, year = target[0], target[1], int(target[2])
    
    day = int(day[0:-1]) # 把10.這種input字串帶有.的部分去除掉
    
    # 先算總天數，總天數 = year * 365 + (month-1) * 20 + day
    total_day = year * 365 + haab.index(month) * 20 + day

    # output format: day, month, year
    # year就是總天數 // 260； month就是總天數mod 260之後再去mod 20看落在哪個月； 日期就是把總天數mod 260之後再去mod 13求出日期的index最後再加1
    print((total_day % 260) % 13+1, tzolkin[(total_day % 260) % 20], total_day // 260)
