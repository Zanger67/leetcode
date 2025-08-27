class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        trie = {}
        for w in words :
            curr = trie
            for c in w :
                if c not in curr :
                    curr[c] = {}
                curr = curr[c]
            # Mark ends of words; +1 in case there are repeats
            curr["."] = curr.get(".", 0) + 1

        for c in s :
            if c not in trie :
                continue
            # Remove the char branch and merge its subtrie contents into main trie
            self._trie_merger_helper(trie, trie.pop(c))

        return trie['.']
            
    def _trie_merger_helper(self, trie1: Dict[str, dict], trie2: Dict[str, dict]) -> None :
        # Merge our "success" counter
        if '.' in trie2 :
            trie1['.'] = trie1.get('.', 0) + trie2.get('.', 0)
            trie2.pop('.')
        
        # Merge branches of trie
        for k, v in trie2.items() :
            if k not in trie1 : # If doesn't exist, we can reuse directly
                trie1[k] = v
                continue
            
            # Recurse into branches
            self._trie_merger_helper(trie1[k], trie2[k])