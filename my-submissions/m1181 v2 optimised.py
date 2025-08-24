class Solution:
    def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:
        output = set()

        # Preprocess second halves
        phrase_keys = defaultdict(list)
        for i, p in enumerate(phrases) :
            k, v = self._first(p)
            phrase_keys[k].append((v, i))


        for i, p1 in enumerate(phrases) :
            start, connector = self._last(p1)

            for ending, j in phrase_keys[connector] :
                if j == i :
                    continue
                output.add(f'{start} {connector} {ending}'.strip())

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