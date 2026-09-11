class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for s in strs:
            chrs = [0] * 26
            for c in s:
                chrs[ord(c) - ord('a')] += 1
            d[tuple(chrs)].append(s)
        
        return list(d.values())