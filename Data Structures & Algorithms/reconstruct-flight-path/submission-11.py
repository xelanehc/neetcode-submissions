class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        tickets.sort()

        for u, v in tickets:
            adj[u].append(v)
        
        res = ["JFK"]

        def dfs(cur):
            if len(res) == len(tickets) + 1:
                return True
            if cur not in adj:
                return False
            
            tmp = list(adj[cur])
            for i, v in enumerate(tmp):
                adj[cur].pop(i)
                res.append(v)
                if dfs(v): return True
                res.pop()
                adj[cur].insert(i, v)
            
            return False
        
        dfs("JFK")
        return res