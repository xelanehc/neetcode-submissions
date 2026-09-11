class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for u, v in sorted(tickets)[::-1]:
            adj[u].append(v)
        
        res = []
        def dfs(cur):
            while adj[cur]:
                dst = adj[cur].pop()
                dfs(dst)
            res.append(cur)
        
        dfs("JFK")
        return res[::-1]