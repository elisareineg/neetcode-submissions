from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        output = []
        adj = defaultdict(list) # course -> prereqs
        if not prerequisites:
            for i in range(numCourses):
                output.append(i)
            return output

        # for each idx in prereq [a,b], add adj[a] = b
        for pair in prerequisites:
            a,b = pair
            adj[a].append(b)

        # dfs into each course, loop through prereqs, add course to visited
        def dfs(course, visited, safe, output):
            if course in visited: # cycle
                return False
            if course in safe:
                return True
            visited.add(course)
            for prereq in adj[course]:
                if not dfs(prereq, visited, safe, output):
                    return False
            visited.remove(course)
            safe.add(course)
            output.append(course)
            return True


        visited = set() # nodes visited in curr DFS call
        safe = set()
        for i in range(numCourses):
            res = dfs(i,visited, safe, output)
            if not res:
                return []
        return output