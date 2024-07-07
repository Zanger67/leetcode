class MyCircularQueue:

    def __init__(self, k: int):
        self.vals = [0] * k
        self.size = 0
        self.pop = 0
        self.add = 0
        self.k = k

    def enQueue(self, value: int) -> bool:
        if self.size >= self.k :
            return False
        if self.size == 0 :
            self.pop = 0
            self.add = 0
            self.vals[0] = value
        else :
            self.add = (self.add + 1) % self.k
            self.vals[self.add] = value
        self.size += 1
        return True
        
    def deQueue(self) -> bool:
        if self.isEmpty() :
            return False

        if self.pop != self.add :
            self.pop = (self.pop + 1) % self.k
        self.size -= 1
        return True

    def Front(self) -> int:
        return self.vals[self.pop] if self.size > 0 else -1

    def Rear(self) -> int:
        return self.vals[self.add] if self.size > 0 else -1
        
    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()