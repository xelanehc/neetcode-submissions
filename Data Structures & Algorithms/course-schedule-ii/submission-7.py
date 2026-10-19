class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {c: [] for c in range(numCourses)}
        indegree = [0] * numCourses
        for u, v in prerequisites:
            adj[u].append(v)
            indegree[v] += 1
        
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        res = []
        total = 0
        while q:
            u = q.popleft()
            res.append(u)
            total += 1
            for nei in adj[u]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        return res[::-1] if total == numCourses else []