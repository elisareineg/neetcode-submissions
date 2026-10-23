class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        arr = []
        n = len(position)
        for idx in range(n):
            arr.append([position[idx], speed[idx]]) # car
        arr = sorted(arr, reverse=True)

        # go through arr and calculate time of each car
        # if curr time <= stack[-1], joins same fleet
        # otherwise, add time to stack
        for i in range(n):
            time = (target - arr[i][0]) / arr[i][1]
            if stack and time <= stack[-1]:
                continue # same fleet
            else:
                stack.append(time)

        return len(stack)
        

        

        
