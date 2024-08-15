class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        register = [0] * 2

        for bill in bills :
            match bill :
                case 5 :
                    register[0] += 1
                case 10 :
                    if not register[0] :
                        return False
                    register[0] -= 1
                    register[1] += 1
                case 20 :
                    if register[1] and register[0] :
                        register[0] -= 1
                        register[1] -= 1
                    elif register[0] >= 3 :
                        register[0] -= 3
                    else :
                        return False
        return True
