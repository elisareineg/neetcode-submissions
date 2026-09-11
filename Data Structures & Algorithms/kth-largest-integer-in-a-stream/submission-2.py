import heapq
"""
class KthLargest:
    # sorting
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.arr = nums

    def add(self, val: int) -> int:
        self.arr.append(val)
        self.arr.sort()
        return self.arr[len(self.arr) - self.k]
"""
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.arr = nums

    def add(self, val: int) -> int:
        heapq.heappush(self.arr, val)
        heapq.heapify(self.arr)
        while len(self.arr) > self.k:
            heapq.heappop(self.arr)
            heapq.heapify(self.arr)
        return self.arr[0]



