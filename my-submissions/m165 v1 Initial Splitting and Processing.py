class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = [int(x) for x in version1.split('.')]
        v2 = [int(x) for x in version2.split('.')]

        if len(v1) < len(v2) :
            v1.extend([0 for _ in range(len(v2) - len(v1))])
        elif len(v1) > len(v2) :
            v2.extend([0 for _ in range(len(v1) - len(v2))])

        for one, two in zip(v1, v2) :
            if one < two :
                return -1

            if two < one :
                return 1
            
        return 0