class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vows   = set('aeiou')
        conses = set(ascii_letters) - vows

        output               = 0        # count of the num of substrings
        consonant_cnt        = 0        # num of consants in current str
        extra_vowels_on_left = 0        # how many vowels on left side of 
                                        # string that aren't required (i.e. 
                                        # we can choose to include them 
                                        # or exclude them)

        indices = deque()   # Deque to keep track of leftmost required char
        vowels = {}         # Tracks right-most occurance of vowel

        for i, c in enumerate(word) :
            if c in vows :
                vowels[c] = i
            else :
                consonant_cnt += 1
            indices.appendleft((i, c))

            # Consonant count must match exactly
            while indices and consonant_cnt > k :
                indx_popped, popped = indices.pop()
                if popped in conses :
                    consonant_cnt -= 1
                elif popped in vows and vowels[popped] == indx_popped :
                    vowels.pop(popped)
                extra_vowels_on_left = 0

            # Remove unnecessary vowels
            while indices and indices[-1][1] in vows and indices[-1][0] != vowels[indices[-1][1]] :
                extra_vowels_on_left += 1
                indices.pop()

            # If extra vowels, we can choose to add x number of vowels to create a new string
            if indices and consonant_cnt == k and len(vowels) == 5 :
                output += 1 + extra_vowels_on_left

        return output