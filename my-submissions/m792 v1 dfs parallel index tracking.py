class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        s_indxes = defaultdict(list)
        for i, c in enumerate(s) :
            s_indxes[c].append(i)

        trie = {}
        for w in words :
            curr = trie
            for c in w :
                if c not in curr :
                    curr[c] = {}
                curr = curr[c]
            # Mark ends of words; +1 in case there are repeats
            curr["."] = curr.get(".", 0) + 1

        return self._dfs_trie(trie, s_indxes, [0] * 26)

    def _dfs_trie(self, 
                  trie: Dict[str, dict], 
                  s_indxes: DefaultDict, 
                  c_indxes: List[int], 
                  curr_indx: int = -1) -> int :
        output = 0
        if "." in trie :
            output += trie["."]

        for nxt_c, nxt_trie in trie.items() :
            if nxt_c not in s_indxes :
                continue
            if nxt_c == "." :
                continue
            char_ord = ord(nxt_c) - ord('a')
            prev_reset = c_indxes[char_ord]

            if c_indxes[char_ord] >= len(s_indxes[nxt_c]) :
                continue

            while s_indxes[nxt_c][c_indxes[char_ord]] < curr_indx :
                c_indxes[char_ord] += 1
                if c_indxes[char_ord] >= len(s_indxes[nxt_c]) :
                    break

            if c_indxes[char_ord] >= len(s_indxes[nxt_c]) :
                c_indxes[char_ord] = prev_reset
                continue

            c_indxes[char_ord] += 1
            output += self._dfs_trie(
                nxt_trie, 
                s_indxes, 
                c_indxes, 
                s_indxes[nxt_c][c_indxes[char_ord] - 1] + 1
            )
            c_indxes[char_ord] = prev_reset

        return output