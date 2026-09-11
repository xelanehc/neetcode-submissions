class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {c: [] for c in range(n)}

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()

        def dfs(cur, parent):
            if cur in visit:
                return False
            
            visit.add(cur)
            for n in adj[cur]:
                if n == parent:
                    continue
                if not dfs(n, cur):
                    return False
            
            return True

        return dfs(0, -1) and len(visit) == n