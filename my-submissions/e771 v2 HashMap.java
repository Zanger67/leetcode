// https://leetcode.com/problems/jewels-and-stones/


class Solution {
    public int numJewelsInStones(String jewels, String stones) {
        HashMap<Character, Integer> cnt = new HashMap<>();

        for (Character c : stones.toCharArray()) {
            cnt.put(c, cnt.getOrDefault(c, 0) + 1);
        }

        int counter = 0;
        for (Character c : jewels.toCharArray()) {
            counter += cnt.getOrDefault(c, 0);
        }

        return counter;
    }
}