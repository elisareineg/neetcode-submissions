class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1 # safe for incrementing
        
        sortedS = sorted(d, key=d.get, reverse=True)
        return sortedS[:k]

