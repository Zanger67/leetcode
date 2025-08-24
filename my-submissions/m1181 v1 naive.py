class Solution:
    def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:
        output = set()

        for i, p1 in enumerate(phrases) :
            a, b = self._last(p1)
            for j, p2 in enumerate(phrases) :
                if i == j :
                    continue
                c, d = self._first(p2)

                if b == c :
                    output.add(f'{a} {b} {d}'.strip())


        return sorted(list(output))

    def _first(self, s: str) -> Tuple[str, str] :
        x = s.find(" ")
        if x == -1 :
            return (s, "")
        return (s[:x].strip(), s[x:].strip())
    def _last(self, s: str) -> Tuple[str, str] :
        x = s.rfind(" ")
        if x == -1 :
            return ("", s)
        return (s[:x].strip(), s[x:].strip())