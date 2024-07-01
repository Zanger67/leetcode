// Space efficiency O(1)
class Solution {
    public int numJewelsInStones(String jewels, String stones) {
        int counter = 0;

        for (Character stn : stones.toCharArray()) {
            for (Character jw : jewels.toCharArray()) {
                if (stn == jw) {
                    counter++;
                }
            }
        }
        return counter;
    }
}