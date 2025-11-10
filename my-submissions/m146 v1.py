class LRUCache:

    def __init__(self, capacity: int):
        self.key_ord = deque()
        self.data = {}
        self.cap = capacity
        self.cnt = {}

    def get(self, key: int) -> int:
        if key in self.data :
            self.cnt[key] += 1
            self.key_ord.appendleft(key)
            return self.data[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.data :
            self.data[key] = value
            self.cnt[key] += 1
            self.key_ord.appendleft(key)
            return
        
        while len(self.data) >= self.cap :
            nxt_pop = self.key_ord.pop()
            self.cnt[nxt_pop] -= 1
            if self.cnt[nxt_pop] == 0 :
                self.cnt.pop(nxt_pop)
                self.data.pop(nxt_pop)
        
        self.data[key] = value
        self.cnt[key] = 1
        self.key_ord.appendleft(key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)