# https://leetcode.com/problems/find-the-n-th-value-after-k-seconds/description/
# https://leetcode.com/contest/weekly-contest-401/

class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        output = [1] * n
        
        for _ in range(k) :
            for j in range(1, n) :
                output[j] += output[j - 1]
        return output[-1] % (10 ** 9 + 7)
        
        
        
''' I DID NOT EXPECT BRUTE FORCE TO WORK-
    
    I wasted so much time trying to find the math behind it lol
    1	1	1	1
    1	2	3	4
    1	3	6	10
    1	4	10	20

    0 [0]			[1]			[2]			[3]
    1 [0]			[0]+[1]			a+b+c   =0+1+2		a+b+c+d		=0+1+2+3
    2 [0]			0+0+1=2a+b		3a+2b+c = 0+0+1+0+1+2	4a+3b+2c+d	=0+0+1+0+1+2+0+1+2+3	
    3 [0]			3a+b			6a+3b+c			10a+6b+3c+d
    4 [0]			4a+b			10a+4b+c		20a+10b+4c+d
    5 [0]									
    6 [0]						
    7 [0]			
    0			
                1*prev + a		2 * prev 

'''