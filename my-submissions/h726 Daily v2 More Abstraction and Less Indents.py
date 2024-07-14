class Solution:
    def countOfAtoms(self, formula: str) -> str:
        return ''.join(sorted([f'{el}{freq}' if freq > 1 
                                             else el for el, freq in self.helper(formula).items()]))

    def getEndIndx(self, formula, indx) -> int :
        openCount = 1
        while openCount > 0 :
            indx += 1
            if formula[indx] == ')' :
                openCount -= 1
            elif formula[indx] == '(' :
                openCount += 1
        return indx

    def getNumber(self, formula, indx) -> Tuple[int, int] : # (multiplier, new indx)
        multiplier = 0
        while indx < len(formula) and re.match('\d', formula[indx]) :
            multiplier = 10 * multiplier + int(formula[indx])
            indx += 1
        
        return (max(multiplier, 1), indx)


    def helper(self, formula: str) -> Counter :
        output = Counter()
        indx = 0

        while indx < len(formula) :

            # Bracketed portion so recurs it
            if formula[indx] == '(' :
                # Find ending of this bracket
                endIndx = self.getEndIndx(formula, indx)

                # Recurs
                cnt = self.helper(formula[indx + 1 : endIndx])

                # Get multiplier e.g. (He2O4)6 multiplier would be 6
                multiplier, indx = self.getNumber(formula, endIndx + 1)

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
                    oldIndx = indx
                    cnt, indx = self.getNumber(formula, indx)
                    output[el] += cnt
        # Helper output
        return output