# https://leetcode.com/problems/replace-words/description/?envType=daily-question&envId=2024-06-07

# V2 using Trie method that consistently hits 98% runtime but hovers around 60% memory

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        
        # Trie setup
        trie = {}
        for root in dictionary :
            current = trie
            for c in root :
                if c in current :
                    current = current[c]
                else :
                    current[c] = {}
                    current = current[c]
            current['!'] = True # signifify end of dict word


        # Output calculation making use of trie
        output = sentence.split(' ')
        for i in range(len(output)) :
            current = trie
            progress = []

            for c in output[i] :
                if current.get('!', False): # Found shortest prefix
                    output[i] = ''.join(progress)
                    break
                if c in current :
                    progress.append(c)
                    current = current[c]
                    continue
                break

        return ' '.join(output)