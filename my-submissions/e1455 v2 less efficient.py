# Bit less efficient but thought it would be fun to code it this way

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        wordStart = 0
        counter = 1

        while True :
            if sentence[wordStart:wordStart + len(searchWord)] == searchWord :
                return counter

            counter += 1
            wordStart = sentence.find(' ', wordStart) + 1
            
            if not wordStart :
                break

        return -1