class Solution:
    # my O(n) solution
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = {}
        for i in nums:
            if i in s:
                return True
            s[i] = 1
        return False
        

    ## Other Solution (On^2):
    """
    for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False
    """