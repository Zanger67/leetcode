class Solution:
    # _pm_dfs stands for premature dfs
    def _pm_dfs(self, rem: int, n: int, output: List[str]) -> str :
        if not n :
            return ''.join(output)

        pot_per_path = 2 ** (n - 1)
        (options := ['a', 'b', 'c']).remove(output[-1])

        if rem <= pot_per_path :
            output.append(options[0])
            return self._pm_dfs(rem, n - 1, output)
        output.append(options[1])
        return self._pm_dfs(rem - pot_per_path, n - 1, output)

    def getHappyString(self, n: int, k: int) -> str:
        n -= 1
        pot_n_min_1 = 2 ** n

        match (k - 1) // pot_n_min_1 :
            case 0 :
                return self._pm_dfs(k, n, ['a'])
            case 1 :
                return self._pm_dfs(k - pot_n_min_1, n, ['b'])
            case 2 :
                return self._pm_dfs(k - 2 * pot_n_min_1, n, ['c'])
            case _ :
                return ''
