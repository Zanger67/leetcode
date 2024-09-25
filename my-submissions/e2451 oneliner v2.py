class Solution:
    def oddString(self, words: List[str]) -> str:
      return {tuple(ord(word[i]) - ord(word[i - 1]) for i in range(1, len(word))) : word for word in words}[sorted(list(Counter(tuple(ord(word[i]) - ord(word[i - 1]) for i in range(1, len(word))) for word in words)), key=lambda x: Counter(tuple(ord(word[i]) - ord(word[i - 1]) for i in range(1, len(word))) for word in words)[x])[0]]
