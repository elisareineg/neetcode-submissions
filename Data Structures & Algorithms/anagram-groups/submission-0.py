
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list) # dictionary without having to init. keys
        for i in strs:
            sortedS = ''.join(sorted(i)) # concatenate it into single string based on sorted letters
            d[sortedS].append(i)
        return list(d.values())
