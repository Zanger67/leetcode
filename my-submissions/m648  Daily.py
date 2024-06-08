# https://leetcode.com/problems/replace-words/description/?envType=daily-question&envId=2024-06-07
# Daily

# Consistently pre slow at 20% percentile :l
# Makes sense as a brute force method to do a trie tho lol

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        output = sentence.split(' ')
        dictionary.sort(key=lambda x: len(x)) 
        for i in range(len(output)) :
            for dictVal in dictionary :
                if len(dictVal) <= len(output[i]) and dictVal == output[i][:len(dictVal)] :
                    output[i] = dictVal
                    break

        return ' '.join(output)