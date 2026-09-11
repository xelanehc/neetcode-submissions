class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict()
        for i in nums:
            freq[i] = freq.get(i, 0) + 1
        sortFreq = sorted(freq, key=freq.get, reverse=True)
        res = []
        for i in range(k):
            res.append(sortFreq[i])
        return res