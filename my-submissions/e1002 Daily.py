# Daily
# Doing this with bad wifi so I can barely submit so idc about efficiency lol


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        cnter = []

        for word in words :
            cnter.append(Counter(word))

        output = []
        primary = cnter[0]

        for ky in primary.keys() :
            minn = primary[ky]
            for i in range(1, len(cnter)) :
                if cnter[i].get(ky, 0) == 0 :
                    minn = 0
                    break
                minn = min(cnter[i].get(ky, 0), minn)
            output += [ky] * minn

        return output
