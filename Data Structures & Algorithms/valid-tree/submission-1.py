class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False

        adj = {c: [] for c in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set()
        
        def cycle(cur, parent):
            if cur in visited:
                return False
            visited.add(cur)
            for nei in adj[cur]:
                if nei == parent:
                    continue
                if not cycle(nei, cur):
                    return False
            return True


        return cycle(0, -1) and len(visited) == n