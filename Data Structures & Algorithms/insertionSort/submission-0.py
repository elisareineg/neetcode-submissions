# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        # Initialize the list to store intermediate steps
        steps = []
        
        # Iterate through the list
        for i in range(len(pairs)):
            # Store the current pair
            current_pair = pairs[i]
            j = i - 1
            
            # Move elements of pairs[0..i-1] that are greater than the current key
            # to one position ahead of their current position
            while j >= 0 and pairs[j].key > current_pair.key:
                pairs[j + 1] = pairs[j]
                j -= 1
            
            # Insert the current pair in the correct position
            pairs[j + 1] = current_pair
            
            # Append the current state of the list to steps
            steps.append([Pair(p.key, p.value) for p in pairs])
        
        return steps