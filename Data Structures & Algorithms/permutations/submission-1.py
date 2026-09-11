class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        picked = set()
        cur = []
        def dfs():
            if len(cur) == len(nums):
                res.append(cur.copy())
                return
            
            for n in nums:
                if n not in picked:
                    picked.add(n)
                    cur.append(n)
                    dfs()
                    cur.pop()
                    picked.remove(n)
        
        dfs()
        return res
