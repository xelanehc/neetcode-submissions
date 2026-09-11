class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret = []
        d = defaultdict(list)
        for s in strs:
            sort = "".join(sorted(s))
            d[sort].append(s)
        for k in d.keys():
            ret.append(d[k])
        return ret