class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.r = 0
        self.c = 0
        self.rows = height
        self.cols = width
        self.score = 0
        self.body = deque()
        self.bodySet = set()

        self.score = 0

        self.food = food
        self.foodIndx = 0

        self.body.append((0, 0))
        self.bodySet.add((0, 0))
        
    def died(self) -> bool :
        if not (0 <= self.r < self.rows) or not (0 <= self.c < self.cols) :
            return True

        if (self.r, self.c) in self.bodySet :
            return True

        return False
    

    def move(self, direction: str) -> int:
        match direction :
            case 'R' :
                self.c += 1
            case 'L' :
                self.c -= 1
            case 'U' :
                self.r -= 1
            case 'D' :
                self.r += 1
            case _ :
                print('ERROR')
        

        if self.foodIndx < len(self.food) and \
            self.r == self.food[self.foodIndx][0] and \
            self.c == self.food[self.foodIndx][1] :
            
            self.foodIndx += 1
            self.score += 1
        else :
            lastSnakeNode = self.body.popleft()
            self.bodySet.remove(lastSnakeNode)

        if self.died() :
            return -1

        self.body.append((self.r, self.c))
        self.bodySet.add((self.r, self.c))

        return self.score
                

        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)