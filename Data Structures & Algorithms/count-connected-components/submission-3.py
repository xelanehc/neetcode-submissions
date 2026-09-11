class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {c: [] for c in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visit = set()
        def dfs(i):
            for n in adj[i]:
                if n not in visit:
                    visit.add(n)
                    dfs(n)

        res = 0
        for i in range(n):
            if i not in visit:
                visit.add(i)
                dfs(i)
                res += 1
        return res