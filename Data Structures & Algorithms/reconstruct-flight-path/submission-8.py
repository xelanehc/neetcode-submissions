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
            
            temp = adj[cur].copy()
            for i, v in enumerate(temp):
                res.append(v)
                adj[cur].pop(i)
                if dfs(v):
                    return True
                adj[cur].insert(i, v)
                res.pop()
            
            return False

        dfs("JFK")
        return res
