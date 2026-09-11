class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {c: [] for c in range(numCourses)}
        for u, v in prerequisites:
            adj[u].append(v)
        
        visit = set()
        def dfs(cur):
            if cur in visit:
                return False
            if not adj[cur]:
                return True
            
            visit.add(cur)
            for neighbor in adj[cur]:
                if not dfs(neighbor):
                    return False
            visit.remove(cur)
            adj[cur] = []
            return True
        
        for node in adj:
            if not dfs(node):
                return False
        return True
        