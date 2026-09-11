class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {c: [] for c in range(numCourses)}
        for k, v in prerequisites:
            adj[k].append(v)
        res = []
        visit, cycle = set(), set()
        def dfs(cur):
            if cur in cycle:
                return False
            if cur in visit:
                return True
            cycle.add(cur)
            for nei in adj[cur]:
                if not dfs(nei):
                    return False
            cycle.remove(cur)
            visit.add(cur)
            res.append(cur)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res