class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 0:
            return 0
        if len(stones) == 1:
            return stones[0]

        while len(stones) > 1:
            # Sort the stones in ascending order
            stones.sort()
            # Get the two heaviest stones
            x, y = stones[-1], stones[-2]
            # Remove the two heaviest stones
            stones.pop()
            stones.pop()
            # Calculate the new stone's weight
            if x != y:
                stones.append(abs(x - y))  # Append the difference

        # Return the last remaining stone, or 0 if no stones are left
        return stones[0] if stones else 0