class TimeMap:

    def __init__(self):
        self.values = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.values:
            self.values[key].append((value,timestamp))
        else:
            self.values[key] = [(value,timestamp)]
        

    def get(self, key: str, timestamp: int) -> str:
        result = ""
        if key in self.values:
            for value,val_timestamp in self.values[key]:
                if val_timestamp <= timestamp:
                    result = value
        return result

        
