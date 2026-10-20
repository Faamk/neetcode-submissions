import bisect

class TimeMap:

    def __init__(self):
        self.values = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.values :
            self.values[key]= ([],[])
        self.values[key][0].append(timestamp)
        self.values[key][1].append(value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.values:
            return ""

        timestamps = self.values[key][0]
        idx = bisect.bisect_right(timestamps, timestamp) - 1

        if idx >= 0:
            return self.values[key][1][idx]
        return ""

        
