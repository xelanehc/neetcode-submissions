class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret = defaultdict(list)
        for s in strs:
            sortS = ''.join(sorted(s))
            ret[sortS].append(s)
        return list(ret.values())