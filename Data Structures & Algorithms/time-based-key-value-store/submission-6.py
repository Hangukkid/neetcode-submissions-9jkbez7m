class TimeMap:

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if (key not in self.timeMap):
            self.timeMap[key] = []
        
        self.timeMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if (key not in self.timeMap):
            return ""
        
        if (self.timeMap[key][0][0] > timestamp):
            return ""
        
        values = self.timeMap[key]
        l, r = 0, len(values) - 1

        res = values[0][1]
        while (l <= r):
            mid = (l + r) // 2
            if (values[mid][0] < timestamp):
                res = values[mid][1]
                l = mid + 1
            elif (values[mid][0] == timestamp):
                res = values[mid][1]
                break
            else:
                r = mid - 1
        
        return res
        
