class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # nums is sorted
        left, right = 0, len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] < target:
                left += 1
            if numbers[left] + numbers[right] > target:
                right -= 1
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            # remember that left and right can switch, aka, right
            # can become the left pointer if subtracted enough, same w/ left pointer
            # to find the right index
        return -1