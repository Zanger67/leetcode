class Solution:
    def countOfAtoms(self, formula: str) -> str:
        def helper(formula: str) -> Counter :
            output = Counter()
            indx = 0

            while indx < len(formula) :

                # Bracketed portion so recurs it
                if formula[indx] == '(' :

                    # Find ending of this bracket
                    endIndx = indx
                    openCount = 1
                    while openCount > 0 :
                        endIndx += 1
                        if formula[endIndx] == ')' :
                            openCount -= 1
                        elif formula[endIndx] == '(' :
                            openCount += 1

                    # Recurs
                    cnt = helper(formula[indx + 1 : endIndx])

                    # Get multiplier e.g. (He2O4)6 multiplier would be 6
                    multiplier = 0
                    indx = endIndx + 1
                    while indx < len(formula) and re.match('\d', formula[indx]) :
                        multiplier = multiplier * 10 + int(formula[indx])
                        indx += 1

                    # If nothing, defaults to 1 instance
                    multiplier = max(multiplier, 1)

                    for el, freq in cnt.items() :
                        output[el] += freq * multiplier

                # Element found
                else :
                    el = ''
                    
                    # 2 letter element
                    if re.match('[A-Z][a-z]', formula[indx : min(indx + 2, len(formula))]) :
                        el = formula[indx : indx + 2]
                        indx += 2
                    # 1 letter element
                    else :
                        el = formula[indx]
                        indx += 1

                    # If next isn't number
                    if indx >= len(formula) \
                        or re.match('[A-Z]', formula[indx]) \
                        or formula[indx] == '(' :
                        output[el] += 1
                    # If is number, find count
                    else :
                        cnt = 0
                        while indx < len(formula) and re.match('\d', formula[indx]) :
                            cnt = 10 * cnt + int(formula[indx])
                            indx += 1
                        output[el] += cnt
            # Helper output
            return output

        return ''.join(sorted([f'{el}{freq}' if freq > 1 
                                             else el for el, freq in helper(formula).items()]))
