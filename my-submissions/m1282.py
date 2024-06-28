class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        people = sorted([(groupSizes[i], i) for i in range(len(groupSizes))], reverse=True)
        outputs = []

        while people :
            currSize = people[-1][0]
            outputs.append([people.pop()[1] for _ in range(currSize)])

        return outputs