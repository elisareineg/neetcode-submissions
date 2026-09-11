class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # must take minimum height[i] of the 2 containers for height
        # width is b/w the 2 bars (j - i)

        l, r = 0, len(heights) - 1
        res = 0

        while l < r:
            if heights[l] < heights[r]:
                area = (r-l) * min(heights[l], heights[r]) # width * height
                res = max(res, area) 
                l += 1
            else:
                area = (r-l) * min(heights[l], heights[r])
                res = max(res, area)
                r -= 1
            

        return res