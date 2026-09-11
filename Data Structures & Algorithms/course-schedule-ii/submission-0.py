class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for u, v in prerequisites:
            adj[u].append(v)

        visited, cycle = set(), set()
        res = []
        
        def dfs(cur):
            if cur in cycle:
                return False
            if cur in visited:
                return True
            cycle.add(cur)
            for pre in adj[cur]:
                if dfs(pre) == False:
                    return False
            cycle.remove(cur)
            visited.add(cur)
            res.append(cur)
            return True
                

        for i in range(numCourses):
            if dfs(i) == False:
                return []
        return res