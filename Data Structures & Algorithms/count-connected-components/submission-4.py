class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visit = set()
        adj = {c: [] for c in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(cur, parent):
            for n in adj[cur]:
                if n == parent:
                    continue
                if n not in visit:
                    visit.add(n)
                    dfs(n, cur)
        
        res = 0
        for i in range(n):
            if i not in visit:
                res += 1
                visit.add(i)
                dfs(i, -1)
        
        return res