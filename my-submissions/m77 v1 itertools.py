# Most straight forwards method given python avalibility :v
# Also by farrrrrr the most efficient since it's a built-in function
# and shows as such in the runtime percentages

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return itertools.combinations(list(range(1, n + 1)), k)