class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        tryLen = 0

        # set str1 as shorter
        if len(str1) > len(str2) :
            str1, str2 = str2, str1

        while tryLen < len(str1) and str1[tryLen] == str2[tryLen] :
            tryLen += 1

        # len of x
        for i in range(tryLen, -1, -1) :
            if not i :
                break

            if len(str1) % i or len(str2) % i :
                continue

            if any(str1[j] != str1[j % i] or 
                   str2[j] != str1[j % i] for j in range(i, len(str1))) :
                continue

            if any(str2[j] != str2[j % i] for j in range(len(str1), len(str2))) :
                continue

            return str1[:i]

        return ''
