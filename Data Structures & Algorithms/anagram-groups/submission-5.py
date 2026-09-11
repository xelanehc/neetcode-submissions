class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            sort = "".join(sorted(s))
            d[sort].append(s)
        return list(d.values())