class Vector2D:
    currentPos = 0
    currentVec = 0
    vec = [[]]
    def __init__(self, vec: List[List[int]]):
        self.vec = vec
        for i in range(0, len(vec)):
            if (len(self.vec[i]) > 0):
                self.currentVec = i
                return

        self.currentPos = -1
        self.currentVec = -1


    def next(self) -> int:
        pos = self.currentPos
        vec = self.currentVec

        self.findNext()

        return self.vec[vec][pos]


        

    def hasNext(self) -> bool:
        return not (self.currentPos == -1 and self.currentVec == -1)
        

    def findNext(self):
        if (self.currentPos < len(self.vec[self.currentVec]) - 1) :
            self.currentPos += 1
            return

        self.currentVec += 1
        self.currentPos = 0

        # find new vector position
        while (self.currentVec < len(self.vec) and len(self.vec[self.currentVec]) == 0) :
            self.currentVec += 1

        if (not self.currentVec < len(self.vec)) :
            self.currentPos = -1
            self.currentVec = -1


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()