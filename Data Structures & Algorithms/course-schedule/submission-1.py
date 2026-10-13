from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj = defaultdict(list) # course -> prereqs
        if not prerequisites:
            return True

        # for each idx in prereq [a,b], add adj[a] = b
        for pair in prerequisites:
            a,b = pair
            adj[a].append(b)

        # dfs into each course, loop through prereqs, add course to visited
        def dfs(course, visited, safe):
            if course in visited: # cycle
                return False
            if course in safe:
                return True
            visited.add(course)
            for prereq in adj[course]:
                if not dfs(prereq, visited, safe):
                    return False
            visited.remove(course)
            safe.add(course)
            return True

            
        visited = set() # nodes visited in curr DFS call
        safe = set()
        for i in range(numCourses):
            res = dfs(i,visited, safe)
            if not res:
                return False
        return True

