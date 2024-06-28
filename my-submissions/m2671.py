class FrequencyTracker:

    def __init__(self):
        self.valToFrequency = defaultdict(int)
        self.frequencyFrequencies = defaultdict(int)

    def add(self, number: int) -> None:
        if self.valToFrequency[number] != 0 :
            self.frequencyFrequencies[self.valToFrequency[number]] -= 1
        self.valToFrequency[number] += 1
        self.frequencyFrequencies[self.valToFrequency[number]] += 1

    def deleteOne(self, number: int) -> None:
        if self.valToFrequency[number] <= 0 :
            return

        self.frequencyFrequencies[self.valToFrequency[number]] -= 1
        self.valToFrequency[number] -= 1
        if self.valToFrequency[number] > 0 :
            self.frequencyFrequencies[self.valToFrequency[number]] += 1
        
    def hasFrequency(self, frequency: int) -> bool:
        return self.frequencyFrequencies[frequency] > 0


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)