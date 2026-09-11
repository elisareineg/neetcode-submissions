class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Optimal
        res = len(nums)  # Initialize res to the length of nums

        for i in range(len(nums)):  # Iterate through the indices of nums
            res += i - nums[i]  # Add the difference between the index and the value at that index to res

        return res  


        #Bitwise
        n = len(nums)
        xorr = n  
        for i in range(n):
            xorr ^= i ^ nums[i]
        return xorr
