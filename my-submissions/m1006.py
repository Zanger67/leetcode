class Solution:
    def clumsy(self, n: int) -> int:
        match n :
            case 4 :
                return 7
            case 3 :
                return 6
            case 2 | 1 | 0 :
                return n
            
        output = n + 1

        match n % 4 :
            case 3 :
                output -= 2
            case 2 :
                output += 1
            case 1 :
                output += 1
            case 0 : 
                output = output
        return output


''' 12 = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1
    12 = 90 / 8 	+ 7 - 30 / 4	+ 3 - 2
    12 = 11		+ 7 - 7		+ 3 - 2

    Don't the values begin to cancel out

    20    = 20 * 19 / 18 + 17 - 16 * 15 / 14 + 13 - 12 * 11 / 10 + 9 - 8 * 7 / 6 + 5 - 4 * 3 / 2 + 1
        21	     + 17 - 17		 + 13 - 13	     + 9 - 9	     + 5 - 6 + 1
        21	     + 17 - 17		 + 13 - 13	     + 9 - 9	     + 5 - 5

    8 = 8 * 7 / 6 + 5 - 4 * 3 / 2 + 1
    = 9 	      + 5 - 6 + 1
    7 = 7 * 6 / 5 + 4 - 3 * 2 / 1
        8         + 4 - 6
    6 = 6 * 5 / 4 + 3 - 2 * 1
        7         + 3 - 2
    5 = 5 * 4 / 3 + 2 - 1
        6         + 2 - 1
    4 = 4 * 3 / 2 + 1
        (5 + 1) + 1 = 7
    3 = 3 * 2 / 1 = 6
    2 = 2 * 1 = 2
'''
