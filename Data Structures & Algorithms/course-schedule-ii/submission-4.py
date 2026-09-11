class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {c: [] for c in range(numCourses)}
        for u, v in prerequisites:
            adj[u].append(v)
        
        visit = set()
        cycle = set()

        def dfs(cur):
            if cur in visit:
                return True
            if cur in cycle:
                return False
            cycle.add(cur)
            for n in adj[cur]:
                if not dfs(n):
                    return False
            cycle.remove(cur)
            visit.add(cur)
            res.append(cur)
            return True
        
        res = []
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res