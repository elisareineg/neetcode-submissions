class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Sorting O(nlogn)
        A = []
        for i, num in enumerate(nums):
            A.append([num, i])
        
        A.sort()
        i, j = 0, len(nums) - 1
        while i < j:
            cur = A[i][0] + A[j][0]
            if cur == target:
                return [min(A[i][1], A[j][1]), 
                        max(A[i][1], A[j][1])]
            elif cur < target:
                i += 1
            else:
                j -= 1
        return []



        # Hash Map Two Pass O(n)
        indices = {}  # val -> index

        for i, n in enumerate(nums):
            indices[n] = i # i is the index, n is the value at that index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in indices and indices[diff] != i:
                return [i, indices[diff]]

        # Hashmap One Pass O(n)



class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val -> index

        for i, n in enumerate(nums): # i is the index, n is the value at that index
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
                