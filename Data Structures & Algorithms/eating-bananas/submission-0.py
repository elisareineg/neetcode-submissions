from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        best = float('inf')
        def totalHours(speed):
            # return total hours for this speed
            total = 0
            for pile in piles:
                total += ceil(pile / speed)
            return total
        # ceil(p/k)
        # totalHours = sum of ceil(pile/k)
        l, r = 1, max(piles) # min rate, max rate (if h < max(piles), thats upper bound)
        while l <= r:
            mid = (l + r) // 2
            curr = totalHours(mid)
            if curr <= h: # works, try to find smaller
                if mid < best:
                    best = mid
                r = mid - 1
            if curr > h:
               l = mid + 1

        return best