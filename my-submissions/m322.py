class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def recurs(amount: int) -> int :
            if amount == 0 :
                return 0
            minn = inf

            # goes in sorted order
            for c in coins :
                if amount - c < 0 :
                    break
                minn = min(minn, recurs(amount - c))
                if minn == 0 :
                    break

            return minn + 1

        coins.sort()

        # Is cached so it recalling it isn't a big deal
        return recurs(amount) if recurs(amount) != inf else -1
