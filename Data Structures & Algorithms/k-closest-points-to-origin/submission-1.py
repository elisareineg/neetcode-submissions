import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # loop through points, find distance, push (point, distance) to minHeap
        # while len(minHeap) > k, pop the points and add to pq
        pq = []
        for point in points:
            dist = math.sqrt(pow(point[0], 2) + pow(point[1],2))
            pq.append((dist, point))

        heapq.heapify(pq)
        res = []
        while len(res) < k:
            dist, point = heapq.heappop(pq)
            res.append(point)
        return res