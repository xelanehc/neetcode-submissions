class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {c: [] for c in range(numCourses)}
        for u, v in prerequisites:
            adj[u].append(v)
        
        visit = set()
        def dfs(cur):
            if cur in visit:
                return False
            visit.add(cur)
            for n in adj[cur]:
                if not dfs(n):
                    return False
            visit.remove(cur)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True