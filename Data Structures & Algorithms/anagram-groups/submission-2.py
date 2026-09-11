class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            d[sortedS].append(s)
        return list(d.values())

