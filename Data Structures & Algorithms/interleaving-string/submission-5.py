class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp = {}

        def dfs(i, j, k):
            if k == len(s3):
                return i == len(s1) and j == len(s2)

            if (i, j, k) in dp:
                return dp[(i, j, k)]
            
            dp[(i, j, k)] = False
            if i < len(s1) and s1[i] == s3[k]:
                dp[(i, j, k)] = dfs(i + 1, j, k + 1)
            if j < len(s2) and s2[j] == s3[k]:
                dp[(i, j, k)] = dfs(i, j + 1, k + 1)
            return dp[(i, j, k)]
        

        return dfs(0, 0, 0)