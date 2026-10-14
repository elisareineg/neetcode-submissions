class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1 = {} # count occurrences of each letter in s1 
        freq2 = {} # "" for s2
        if len(s1) > len(s2):
            return False
        
        for i in s1:
            freq1[i] = freq1.get(i, 0) + 1

        for i in range(len(s1)):
            freq2[s2[i]] = freq2.get(s2[i], 0) + 1
        if freq1 == freq2:
            return True

        for r in range(len(s1), len(s2)):
            freq2[s2[r]] = freq2.get(s2[r], 0) + 1
            freq2[s2[r - len(s1)]] -= 1 # left ptr
            count = freq2[s2[r - len(s1)]] 
            if count == 0:
                del(freq2[s2[r-len(s1)]])
            if freq1 == freq2:
                return True
        return False


        
        
