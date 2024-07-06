class Solution {
    public int passThePillow(int n, int time) {
        time %= 2 * (n - 1);
        if (time < n)
            return time + 1;
        time -= n - 1;
        return n - time;
    }
}