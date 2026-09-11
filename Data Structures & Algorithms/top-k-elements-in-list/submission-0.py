class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict()
        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        sortFreq = sorted(freq, key=freq.get, reverse=True)
        res = []
        for i in range(k):
            res.append(sortFreq[i])
        return res