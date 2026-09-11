class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {c: [] for c in range(numCourses)}
        for k, v in prerequisites:
            adj[k].append(v)
        visit = set()
        def dfs(cur):
            if cur in visit:
                return False
            if adj[cur] == []:
                return True
            visit.add(cur)
            for nei in adj[cur]:
                if not dfs(nei):
                    return False
            visit.remove(cur)
            adj[cur] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True