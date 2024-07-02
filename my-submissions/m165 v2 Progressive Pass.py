class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        one, two = 0, 0

        while one < len(version1) and two < len(version2) :
            oneNew = version1.find('.', one)
            twoNew = version2.find('.', two)

            if oneNew < 0 :
                oneNew = len(version1)
            if twoNew < 0 :
                twoNew = len(version2)

            oneInt = int(version1[one:oneNew])
            twoInt = int(version2[two:twoNew])

            if oneInt < twoInt :
                return -1
            if twoInt < oneInt :
                return 1
            
            one = oneNew + 1
            two = twoNew + 1

        while one < len(version1) :
            oneNew = version1.find('.', one)
            if oneNew < 0 :
                oneNew = len(version1)
            oneInt = int(version1[one:oneNew])

            if oneInt < 0 :
                return -1
            if oneInt > 0 :
                return 1

            one = oneNew + 1

        while two < len(version2) :
            twoNew = version2.find('.', two)
            if twoNew < 0 :
                twoNew = len(version2)
            twoInt = int(version2[two:twoNew])

            if twoInt > 0 :
                return -1
            if twoInt < 0 :
                return 1

            two = twoNew + 1

        return 0