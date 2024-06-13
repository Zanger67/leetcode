# https://leetcode.com/problems/generate-parentheses/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []

        def helper(curr: [], openLeft: int, closeLeft: int) -> None :
            if closeLeft == 0 == openLeft :
                output.append(''.join(curr))
                return

            if openLeft > 0 :
                curr.append('(')
                helper(curr, openLeft - 1, closeLeft)
                curr.pop()

            if closeLeft <= openLeft :
                return

            curr.append(')')
            helper(curr, openLeft, closeLeft - 1)
            curr.pop()

        helper([], n, n)
        return output