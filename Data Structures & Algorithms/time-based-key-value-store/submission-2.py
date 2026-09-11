class TimeMap:

    def __init__(self):
        self.backing = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.backing[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        values = self.backing.get(key, [])
        lo, hi = 0, len(values) - 1
        res = ""
        while lo <= hi:
            mid = lo + ((hi - lo) // 2)
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                lo = mid + 1
            else:
                hi = mid - 1
        return res
        
