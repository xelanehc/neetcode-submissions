class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for s in range(1, len(strs)):
            j = 0

            while j < min(len(prefix), len(strs[s])):
                if prefix[j] != strs[s][j]:
                    break
                j += 1
            
            prefix = prefix[:j]
        
        return prefix