class TimeMap:

    def __init__(self):
        self.vals = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.vals :
            self.vals[key] = [[], []]
        self.vals[key][0].append(value)
        self.vals[key][1].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.vals :
            return ''
        if timestamp < self.vals[key][1][0] :
            return ''
        return self.vals[key][0][bisect_right(self.vals[key][1], timestamp) - 1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
