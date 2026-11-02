from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.keyVal = defaultdict(list) # store key -> (value, timestamp)


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keyVal[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        res = []
        if key in self.keyVal:
            entries = self.keyVal[key] # list of multiple tuples
            lo, hi = 0, len(entries) - 1
            while lo <= hi:
                mid = (lo + hi) // 2
                if entries[mid][1] == timestamp:
                    return entries[mid][0]
                if entries[mid][1] <= timestamp:
                    res.append(entries[mid][0]) # still valid so far
                    lo = mid + 1
                elif entries[mid][1] > timestamp:
                    hi = mid - 1
        return res[-1] if res else "" # highest timestamp or return "" if no values associated
        