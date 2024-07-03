class Solution:
    def isValid(self, word: str) -> bool:
        if not word.isalnum() :
            return False

        if len(word) < 3 :
            return False

        cons, vow = False, False
        vowels = set('aeiou')

        for i, c in enumerate(word) :
            if c.lower() in vowels :
                vow = True
            elif not c.isnumeric() :
                cons = True
            
            if vow and cons :
                return True
        return False