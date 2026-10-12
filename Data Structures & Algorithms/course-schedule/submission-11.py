class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i: [] for i in range(numCourses)}
        for u, v in prerequisites:
            adj[u].append(v)
        seen = set()

        def recurse(u):
            if adj[u] == []:
                return True
            if u in seen:
                return False
            
            seen.add(u)
            for neighbor in adj[u]:
                if not recurse(neighbor):
                    return False
            seen.remove(u)
            adj[u] = []
            return True
        
        for c in range(numCourses):
            if not recurse(c):
                return False

        return True