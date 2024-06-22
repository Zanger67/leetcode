class Solution {
    public int minPartitions(String n) {
        int maxx = 0;

        for (char c : n.toCharArray()) {
            maxx = Integer.max(maxx, c - '0');
        }
        return maxx;
    }
}