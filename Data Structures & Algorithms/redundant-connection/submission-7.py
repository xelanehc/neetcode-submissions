class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = {c: [] for c in range(1, len(edges) + 1)}
        
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
        
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            visited = set()

            if not dfs(u, -1):
                return [u, v]
        
        return []