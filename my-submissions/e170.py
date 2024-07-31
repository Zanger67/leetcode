class TwoSum:

    def __init__(self):
        self.vals = Counter()

    def add(self, number: int) -> None:
        self.vals[number] += 1

    def find(self, value: int) -> bool:
        return any(value - val in self.vals 
                   and (val != value - val or self.vals[value - val] > 1) for val in self.vals)

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)