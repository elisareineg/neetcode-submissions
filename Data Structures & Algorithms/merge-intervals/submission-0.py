class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # inclusive, if end and start == then append
        res = []
        if not intervals:
            return res
        sortedIntervals = sorted(intervals)
        # sort by start, and compare each start to res[-1][1]
        # if <= res[-1][1], then we adjust res[-1] = [res[-1][0], max(res[-1][1], intervals[i][1])]

        for start, end in sortedIntervals:
            if not res:
                res.append([start, end])
                continue

            if start <= res[-1][1]: # merge
                res[-1] = [res[-1][0], max(res[-1][1], end)]

            else: # append normally
                res.append([start, end])

        return res