# https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/description/?envType=daily-question&envId=2024-05-30

''' Notes
    Negation of XOR is Biconditional 
    i.e. p <-> q
    (p -> q) and (q -> p)
    (!p or q) and (!q or p)
    (!p and !q) or (p and q)
    p == q


    1^0 --> 1 -->  --> 1^0 --> 1
    1^1 --> 0 -->  --> 0^1 --> 1
    0^0 --> 0 -->  --> 0^0 --> 0
    0^1 --> 1 -->  --> 1^1 --> 0

    XORing by the same value again reverses the result!

    Since 0 <= i < j <= k < arr.len --> k-i+1 >= 2

    If two arrays XOR together to get 0, then the two individual sections should have
    an XOR that equal each other.

    That is, XOR(arr1) == XOR(arr2) so that XOR(arr1, arr2) == 0
'''

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        counter = 0
        for k in range(len(arr) - 1, 0, -1) :
            current = arr[k]
            for i in range(k - 1, -1, -1) :
                current ^= arr[i]
                if (current == 0) :
                    # counter += 1
                    counter += k - i
        return counter