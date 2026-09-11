class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # monotonic stack
        stack = []
        res = [0] * len(temperatures)

        # start from end of temperatures, move backwards incrementing each time the number at the curr idx is lower than the element at the top of the stack
        # if we get to an element that's higher add the # of days to res and pop from stack
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                idx, t = stack.pop()
                diff = i - idx
                res[idx] = diff

            stack.append((i, temp))
        return res