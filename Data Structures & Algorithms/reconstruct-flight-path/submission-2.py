class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {src: [] for src, dst in tickets}
        tickets.sort()
        for src, dst in tickets:
            adj[src].append(dst)
        res = ["JFK"]
        def dfs(cur):
            if len(res) == len(tickets) + 1:
                return True
            if cur not in adj:
                return False
            temp = list(adj[cur])
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
