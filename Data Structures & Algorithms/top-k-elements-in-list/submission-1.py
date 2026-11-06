from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for i in nums:
            count[i] += 1
        sortedCount = dict(sorted(count.items(), key=lambda item: item[1], reverse=True)) # sort by highest values
        res = [] # add dict keys to result list
        for i in sortedCount:
            if len(res) < k:
                res.append(i)

        return res