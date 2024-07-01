class Solution {
    public int numJewelsInStones(String jewels, String stones) {
        Set<Character> jw = new HashSet<>();
        for (Character c : jewels.toCharArray()) {
            jw.add(c);
        }

        int counter = 0;
        for (Character c : stones.toCharArray()) {
            if (jw.contains(c)) {
                counter++;
            }
        }
        
        return counter;
    }
}