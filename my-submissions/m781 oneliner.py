class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        return sum((freqs + 1) * (ceil(x / (freqs + 1))) for freqs, x in Counter(answers).items())
