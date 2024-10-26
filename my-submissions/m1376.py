class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        subs = defaultdict(list)
        for i, m in enumerate(manager) :
            subs[m].append(i)

        def dfs(subs: dict, informTime: List[int] = informTime, curr: int = headID) -> int :
            return informTime[curr] + max([dfs(subs, informTime, x) for x in subs[curr]] + [0])

        return dfs(subs)
