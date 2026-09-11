class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []
        combination = []

        def dfs(i, s):
            if s == target:
                res.append(combination.copy())
                return
            if i >= len(candidates) or s > target:
                return
            
            s += candidates[i]
            combination.append(candidates[i])
            dfs(i + 1, s)
            s -= candidates[i]
            combination.pop()
            
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, s)
        
        dfs(0, 0)
        return res