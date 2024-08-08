class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        output = [[rStart, cStart]]

        distance = 1        # current side length
        direction = 0       # 0=r, 1=d, 2=l, 3=u
        twice = False

        while len(output) < rows * cols :
            for i in range(1, distance + 1) :
                match direction % 4 :
                    case 0 :
                        cStart += 1
                    case 1 :
                        rStart += 1
                    case 2 :
                        cStart -= 1
                    case 3 :
                        rStart -= 1

                if not (0 <= cStart < cols) or not (0 <= rStart < rows) :
                    continue

                output.append([rStart, cStart])

            direction += 1

            twice = not twice
            if not twice :
                distance += 1

        return output