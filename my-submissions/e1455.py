# https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/description/


class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split(' ')
        for i in range(len(words)) :
            if words[i][:len(searchWord)] == searchWord :
                return i + 1

        return -1