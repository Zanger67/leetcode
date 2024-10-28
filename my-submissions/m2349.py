class NumberContainers:

    def __init__(self):
        self.data = {}
        self.indicies_values = {}

    def change(self, index: int, number: int) -> None:
        if number not in self.data :
            self.data[number] = []
        heapq.heappush(self.data[number], index)

        if index not in self.indicies_values :
            self.indicies_values[index] = number
            return

        prev_val = self.indicies_values[index]
        self.indicies_values[index] = number

        while self.data[prev_val] and self.indicies_values[self.data[prev_val][0]] != prev_val :
            heapq.heappop(self.data[prev_val])

        if not self.data[prev_val] :
            self.data.pop(prev_val)

    def find(self, number: int) -> int:
        if number not in self.data :
            return -1
        return self.data[number][0]


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
