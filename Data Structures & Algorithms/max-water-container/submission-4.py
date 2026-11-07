class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxArea = 0

        # height = min(height[l], height[r]]
        # width = r - l (0 indexed) 
        # so maxArea = max(maxArea, width * height)

        while l <= r:
            area = min(heights[l], heights[r]) * (r - l)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

            maxArea = max(maxArea, area)

        return maxArea