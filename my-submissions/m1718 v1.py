class Solution:
    def helper(self, output: List[int], curr_indx: int, pot_vals: List[int]) -> List[int] | bool :
        # The check for if there are pot_vals remaining is to check
        # whether multiple "1"s were used
        if curr_indx >= len(output) :
            return output if not pot_vals else False

        if output[curr_indx] :
            return self.helper(output, curr_indx + 1, pot_vals)

        len_potvals = len(pot_vals)
        for i in range(len_potvals - 1, -1, -1) :
            # This part is quite inefficient due to it popping and inserting causing many O(n)
            # operations but is somewhat needed in order to keep pot_vals sorted when
            # parsing the potential answers
            if curr_indx + pot_vals[i] < len(output) and not output[curr_indx + pot_vals[i]] :
                curr = pot_vals.pop(i)
                output[curr_indx] = curr
                output[curr_indx + curr] = curr
                pot_result = self.helper(output, curr_indx + 1, pot_vals)

                # if returns a list, then answer found
                # if returns bool FALSE, then invalid case
                if pot_result :
                    return output

                pot_vals.insert(i, curr)
                output[curr_indx] = 0
                output[curr_indx + curr] = 0

        # Insert the "1" case since it appears once
        output[curr_indx] = 1
        pot_result = self.helper(output, curr_indx + 1, pot_vals)
        if pot_result :
            return pot_result
        output[curr_indx] = 0

        return False


    def constructDistancedSequence(self, n: int) -> List[int]:
        output = [0] * (n + n - 1)
        pot_vals = list(range(2, n + 1))

        return self.helper(output, 0, pot_vals)