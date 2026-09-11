class TimeMap:

    def __init__(self):
        self.backing = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.backing[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        for i in range(len(self.backing[key]) - 1, -1, -1):
            val, time = self.backing[key][i]
            if time <= timestamp:
                return val
        return ""
        
