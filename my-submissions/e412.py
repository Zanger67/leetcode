class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        output = []

        for i in range(1, n + 1) :
            if i % 15 == 0 :
                output.append('FizzBuzz')
            elif i % 5 == 0 :
                output.append('Buzz')
            elif i % 3 == 0 :
                output.append('Fizz')
            else :
                output.append(f'{i}')
        
        return output