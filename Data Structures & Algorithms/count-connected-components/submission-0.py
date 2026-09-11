class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {c: [] for c in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set()

        def dfs(cur):
            if cur in visited:
                return
            visited.add(cur)
            for nei in adj[cur]:
                dfs(nei)
            
        res = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                res += 1
        return res