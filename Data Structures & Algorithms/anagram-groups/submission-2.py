from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list) # stores anagram -> words

        for i in range(len(strs)):
            sortedAnagram = "".join(sorted(strs[i]))
            groups[sortedAnagram].append(strs[i])

        return list(groups.values())
