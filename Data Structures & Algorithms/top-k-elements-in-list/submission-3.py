class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for n in nums:
            d[n] += 1
        ret = []
        freq = sorted(d.keys(), key = lambda x: d[x])
        freq = freq[::-1]
        for i in range(k):
            ret.append(freq[i])
        return ret