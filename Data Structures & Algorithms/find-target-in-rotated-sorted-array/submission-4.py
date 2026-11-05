class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l+r) // 2
            # look for min, then split array into 2 partitions for search
            if nums[mid] > nums[r]:
                # min element in right side
                l = mid + 1
            else:
                # min element in left 
                r = mid

        # l = mid element / partition point
        if target <= nums[-1]:
            lo, hi = l, len(nums) - 1
        else:
            lo, hi = 0, l - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] > target:
                hi = mid - 1
            elif nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid + 1

        return -1