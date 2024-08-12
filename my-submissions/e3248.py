class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        x, y = 0, 0
        for c in commands :
            match c :
                case 'DOWN' :
                    y += 1
                case 'UP' :
                    y -= 1
                case 'LEFT' :
                    x -= 1
                case _ :
                    x += 1
        
        return y * n + x
