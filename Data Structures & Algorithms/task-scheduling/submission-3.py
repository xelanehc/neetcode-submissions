class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = defaultdict(int)
        for t in tasks:
            freq[t] += 1

        maxHeap = [-cnt for cnt in freq.values()]
        heapq.heapify(maxHeap)
        q = deque()
        res = 0

        while q or maxHeap:
            res += 1

            if not maxHeap:
                res = q[0][1]
            else:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, res + n])
            if q and q[0][1] == res:
                heapq.heappush(maxHeap, q.popleft()[0])
        
        return res