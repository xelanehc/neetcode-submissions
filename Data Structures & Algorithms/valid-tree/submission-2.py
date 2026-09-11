class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False
        adj = {c: [] for c in range(n)}
        for k, v in edges:
            adj[k].append(v)
            adj[v].append(k)
        
        visited = set()
        def dfs(cur, par):
            if cur in visited:
                return False
            visited.add(cur)
            for nei in adj[cur]:
                if nei == par:
                    continue
                if not dfs(nei, cur):
                    return False
            return True
        
        return dfs(0, -1) and len(visited) == n