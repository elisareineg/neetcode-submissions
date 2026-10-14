class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxArea = 0

        while l < r:
            width = r - l 
            height = min(heights[l], heights[r])
            area = width * height
            if height == heights[r]:
                r-=1
            elif height == heights[l]:
                l += 1
            maxArea = max(maxArea, area)

        return maxArea