class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # linked list cycle: floyd's algorithm
        # because values within 1, n, that means nums[i] will always be valid as an index
        
        slow, fast = 0, 0
        # when slow == head, that index indicates start of the cycle (return val)

        # when cycle is found, make new slow pointer and set to 0, then increment both pointers until they intersect and that's the answer

        while True: 
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        # phase 2 
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow # or slow2
