class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        tempStack = []                      # schema: (temperature, index)

        for i in range(len(temperatures) - 1, -1, -1) :
            while tempStack :
                if tempStack[-1][0] > temperatures[i] :
                    output[i] = tempStack[-1][1] - i
                    break
                else :
                    tempStack.pop()
            
            tempStack.append((temperatures[i], i))

        return output
