class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # the solution asks for O(1) space, so we can't use hash or set
        res = 0
        for num in nums:
            res = num ^ res # Perform XOR operation between the current number and the result
            # if num is the same as res, it will cancel itself out
        return res
