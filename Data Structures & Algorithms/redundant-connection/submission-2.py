class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = {c: [] for c in range(1, len(edges) + 1)}
        
        def dfs(cur, parent):
            if cur in visit:
                return True
            
            visit.add(cur)
            for n in adj[cur]:
                if n == parent:
                    continue
                if dfs(n, cur):
                    return True
            return False
        
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            visit = set()
            if dfs(u, v):
                return [u, v]
            if dfs(v, u):
                return [u, v]