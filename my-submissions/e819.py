class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        cnt = Counter([x.lower() for x in re.findall('[A-Za-z]+', paragraph)])
        banned = set(banned)
        output = sorted([x for x in cnt.keys() if x not in banned], key=lambda x: cnt[x])
        return output[-1]
