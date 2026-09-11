class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]
        for n in nums:
            count[n] += 1
        for num, cnt in count.items():
            freq[cnt].append(num)
        ret = []
        for i in range(len(freq) - 1, 0, -1):
            for j in freq[i]:
                ret.append(j)
                if len(ret) == k:
                    return ret
