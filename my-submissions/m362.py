class HitCounter:

    def __init__(self):
        self.hits = []

    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        indx = bisect_left(self.hits, timestamp)
        cnt = 0

        for i in range(min(indx, len(self.hits) - 1), -1, -1) :
            if abs(self.hits[i] - timestamp) >= 300 :
                break
            cnt += 1
        
        for i in range(indx + 1, len(self.hits)) :
            if abs(self.hits[i] - timestamp) >= 300 :
                break
            cnt += 1
        
        return cnt


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
