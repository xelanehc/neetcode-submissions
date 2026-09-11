class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for k, v in edges:
            adj[k].append(v)
            adj[v].append(k)
        
        visited = set()
        def dfs(cur):
            for nei in adj[cur]:
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei)
        res = 0
        for i in range(n):
            if i not in visited:
                visited.add(i)
                dfs(i)
                res += 1
        return res