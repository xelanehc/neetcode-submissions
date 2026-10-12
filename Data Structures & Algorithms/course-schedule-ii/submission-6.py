class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i:[] for i in range(numCourses)}
        indegree = [0] * numCourses

        for u, v in prerequisites:
            indegree[v] += 1
            adj[u].append(v)
        
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        res = []
        while q:
            cur = q.popleft()
            res.append(cur)
            for nei in adj[cur]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        return res[::-1] if len(res) == numCourses else []