class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        find = set()
        for t in triplets:
            if t[0] <= target[0] and t[1] <= target[1] and t[2] <= target[2]:
                if t[0] == target[0]:
                    find.add(0)
                if t[1] == target[1]:
                    find.add(1)
                if t[2] == target[2]:
                    find.add(2)
        return 0 in find and 1 in find and 2 in find