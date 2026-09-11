class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {c: [] for c in range(numCourses)}
        for u, v in prerequisites:
            adj[u].append(v)
        
        visited = set()

        def dfs(cur):
            if cur in visited:
                return False
            if adj[cur] == []:
                return True
            visited.add(cur)
            for pre in adj[cur]:
                if not dfs(pre):
                    return False
            visited.remove(cur)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False

        return True