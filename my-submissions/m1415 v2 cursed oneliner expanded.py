class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        return (
            _pm_dfs := (
                lambda rem, n, output: 
                    ''.join(output) if not n else 
                    _pm_dfs(
                        rem - (pot_per_path if (indx := int(rem > (pot_per_path := 2 ** (n - 1)))) else 0), 
                        n - 1, 
                        output + ['abc'.replace(output[-1], '')[indx]]
                    )
            )
        )(
            k - x * pot_n_min_1,
            n, 
            [chr(ord('a') + x)]
        ) if (x := (k - 1) // (pot_n_min_1 := 2 ** (n := n - 1))) <= 2 else \
        ''