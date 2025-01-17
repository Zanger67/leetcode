class Solution {
    public boolean doesValidArrayExist(int[] derived) {
        int output = 1;
        for (int i : derived) {
            output ^= i;
        }
        return output == 1;
    }
}