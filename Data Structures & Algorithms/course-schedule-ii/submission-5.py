class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        in_degree = defaultdict(int)

        for crs, pre in prerequisites:
            adj[pre].append(crs)
            in_degree[crs] += 1
        
        q = deque()

        for i in range(numCourses):
            if in_degree[i] == 0:
                q.append(i)
        
        res = []
        while q:
            cur = q.popleft()
            res.append(cur)

            for n in adj[cur]:
                in_degree[n] -= 1
                if in_degree[n] == 0:
                    q.append(n)

        return res if len(res) == numCourses else []