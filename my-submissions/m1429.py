class FirstUnique:

    def __init__(self, nums: List[int]):
        self.queue = deque(nums)
        self.counter = Counter(nums)

        while self.queue and self.counter[self.queue[0]] > 1 :
            self.queue.popleft()

    def showFirstUnique(self) -> int:
        return -1 if not self.queue else self.queue[0]

    def add(self, value: int) -> None:
        self.counter[value] += 1
        self.queue.append(value)
        while self.queue and self.counter[self.queue[0]] > 1 :
            self.queue.popleft()

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
