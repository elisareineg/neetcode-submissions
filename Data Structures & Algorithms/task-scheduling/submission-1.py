import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {} # find most frequent letter in tasks
        maxFreq = 0
        maxHeap = [] # retrieve max element

        for t in tasks:
            freq[t] = freq.get(t, 0) + 1
            if freq[t] > maxFreq:
                maxFreq = freq[t]
        for letter in freq:
            maxHeap.append(-freq[letter]) # add negative ver. to make maxHeap

        heapq.heapify(maxHeap)
        queue = deque() # store tasks, time they become available after cooldown
        time = 0
        while maxHeap or queue:
            time += 1 # idle
            # if maxHeap empty: update time to match next available task
            if maxHeap:
                num = heapq.heappop(maxHeap)
                num += 1
                if num < 0: # task not completed for that letter
                    # if task at front of the queue becomes available, pop and reinsert into heap            
                    queue.append((num, time + n))


            if queue and queue[0][1] == time:
                num, time = queue.popleft()
                heapq.heappush(maxHeap, num)

        return time
            
            
            
            
         