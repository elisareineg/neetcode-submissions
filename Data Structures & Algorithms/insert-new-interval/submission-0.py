class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        intervals.append(newInterval)
        intervals.sort()
        for start, end in intervals:
            if not res:
                res.append([start, end])
                continue

            if start <= res[-1][1]: # merge
                res[-1] = [res[-1][0], max(res[-1][1], end)]

            else: # append normally
                res.append([start, end])

        return res

        
        