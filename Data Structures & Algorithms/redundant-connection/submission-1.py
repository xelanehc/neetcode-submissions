class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = {c: [] for c in range(1, len(edges) + 1)}

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
            visited.remove(cur)
            return True
        
        for k, v in edges:
            adj[k].append(v)
            adj[v].append(k)
            if not dfs(k, v):
                return [k, v]