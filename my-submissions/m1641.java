// This is just stars and bars lol
// n stars, 4 bars
// n + 4 choose 4

class Solution {
    public int countVowelStrings(int n) {
        return (n + 4) * (n + 3) * (n + 2) * (n + 1) / 24;
    }
}