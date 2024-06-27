class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        mappings = defaultdict(List[int])
        starters = set()

        for pair in adjacentPairs :
            if pair[0] in mappings : 
                mappings[pair[0]].append(pair[1])
            else :
                mappings[pair[0]] = [pair[1]]
            
            if pair[1] in mappings :
                mappings[pair[1]].append(pair[0])
            else :
                mappings[pair[1]] = [pair[0]]

            if pair[0] in starters :
                starters.remove(pair[0])
            else :
                starters.add(pair[0])
                
            if pair[1] in starters :
                starters.remove(pair[1])
            else :
                starters.add(pair[1])

        output = [list(starters)[0]]
        while len(output) <= len(adjacentPairs) :
            options = mappings[output[-1]]

            if len(options) <= 1 :
                output.append(options[0])
            elif output[-2] != options[0] :
                output.append(options[0])
            else :
                output.append(options[1])

        return output