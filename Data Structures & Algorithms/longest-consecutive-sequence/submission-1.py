class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0
        for i in nums:
            length = 0 # at each start seq, we will increment while i + 1 is in the set
            if i - 1 not in nums:
                # start = i 
                length += 1
                last = i 
                while last + 1 in nums:
                    last += 1
                    length += 1
            else:
                continue
            longest = max(longest, length)

        return longest
            



