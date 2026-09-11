class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {src: [] for src, dst in tickets}

        tickets.sort()

        for u, v in tickets:
            adj[u].append(v)
        
        res = ["JFK"]
        def dfs(cur):
            if len(res) == len(tickets) + 1:
                return True
            if cur not in adj:
                return False
            
            for i, n in enumerate(adj[cur]):
                res.append(n)
                adj[cur].pop(i)
                if dfs(n):
                    return True
                res.pop()
                adj[cur].insert(i, n)
            
            return False
        
        dfs("JFK")
        return res