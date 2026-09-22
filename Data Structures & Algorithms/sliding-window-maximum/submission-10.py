class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = deque()
        res = []
        l = 0

        for r in range(len(nums)):

            while d and nums[d[-1]] < nums[r]:
                d.pop()
            
            d.append(r)

            if l > d[0]:
                d.popleft()

            if r + 1 >= k:
                res.append(nums[d[0]])
                l += 1
        
        return res