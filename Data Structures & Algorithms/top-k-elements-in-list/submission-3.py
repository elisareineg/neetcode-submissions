from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = defaultdict(int)
        for i in nums:
            frequency[i] += 1
        heap = []
        for i in frequency:
            heap.append((-frequency[i], i)) # store -freq (for max heap), and value
        heapq.heapify(heap)
        time = 0 # track number of times we pop from heap
        res = [] # append to this result list
        while time < k:
            negFreq, value = heapq.heappop(heap)
            res.append(value)
            time += 1
          
        return res






        """
        O(nlogn)
        count = defaultdict(int)
        for i in nums:
            count[i] += 1
        sortedCount = dict(sorted(count.items(), key=lambda item: item[1], reverse=True)) # sort by highest values
        res = [] # add dict keys to result list
        for i in sortedCount:
            if len(res) < k:
                res.append(i)
            else:
                break # saves loop from running 
        return res
        """