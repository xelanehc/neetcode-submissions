class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {c: [] for c in range(n)}

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()

        def dfs(cur, parent):
            if cur not in visit:
                visit.add(cur)
                for n in adj[cur]:
                    if n == parent:
                        continue
                    dfs(n, cur)
        
        res = 0
        for i in range(n):
            if i not in visit:
                res += 1
                dfs(i, -1)

        return res