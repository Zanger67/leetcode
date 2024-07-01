class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        self.output = []
        for i in range(0, numRows) :
            self.output.append([1])

        if (numRows == 1) :
            return self.output
        
        self.output[1].append(1)
        if (numRows == 2) :
            return self.output


        # program starts row 3
        for i in range(2, numRows) :
            for j in range(1, (i + 2) // 2) :
                self.output[i].append(self.output[i-1][j] + self.output[i-1][j - 1])
            self.output[i].extend(reversed(self.output[i][0:((i + 1) // 2)]))

        return self.output
