class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        output = 0
        for freqs, x in Counter(answers).items() :
            output += (freqs + 1) * (ceil(x / (freqs + 1)))
        return output