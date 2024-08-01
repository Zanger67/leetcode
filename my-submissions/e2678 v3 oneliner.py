class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return [True for x in details if int(x[11:13]) > 60].count(True)