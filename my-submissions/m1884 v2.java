class Solution {
    public int twoEggDrop(int n) {
        return (int) (Math.ceil(-0.5 + Math.sqrt(2 * n + 0.25)));
    }
}