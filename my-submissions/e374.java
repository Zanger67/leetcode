// This is just bin search but with casting to long cause of int overflow lol

/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * int guess(int num);
 */

 public class Solution extends GuessGame {
    public int guessNumber(int n) {
        int left = 1, right = n;

        while (left < right) {
            int mid = (int) (((long) left + (long) right) / 2);
            int gs = guess(mid);

            if (gs == 0) {
                return mid;
            }

            if (gs == -1) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return left;
        
    }
}