class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        l, r = 0, len(nums) - 1
        minSoFar = nums[0]
        while l<r:
            # if nums[mid] > nums[r], then min must be in second half
            # if numbs[mid] < nums[l], in left part
            # otherwise, return first element
            mid = (l+r) // 2
            if nums[mid] < nums[r]: 
                # min in left part
                r = mid - 1
                minSoFar = min(minSoFar, nums[mid])

            else:
                # min is in right part
                l = mid + 1
                minSoFar = min(minSoFar, nums[l])


        return minSoFar

       
                