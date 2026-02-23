import bisect
from collections import defaultdict

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        indexes = defaultdict(list)
        for i, char in enumerate(text2):
            indexes[char].append(i)
        
        for char in indexes:
            indexes[char].reverse()
            
        tails = []
        
        for char in text1:
            if char not in indexes:
                continue
            
            for index in indexes[char]:
                pos = bisect.bisect_left(tails, index)
                
                if pos == len(tails):
                    tails.append(index)
                else:
                    tails[pos] = index
                    
        return len(tails)

a = Solution()

while True:
    try:
        text1 = input()
        text2 = input()

        print(a.longestCommonSubsequence(text1, text2))
    except EOFError:
        break
