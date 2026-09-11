class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = {c: [] for c in range(1, len(edges) + 2)}

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

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            visit = set()

            if not dfs(u, -1):
                return [u, v]