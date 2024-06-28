class Solution {
    public long maximumImportance(int n, int[][] roads) {
        int[] cnt = new int[n];

        for (int[] road : roads) {
            cnt[road[0]]++;
            cnt[road[1]]++;
        }
        Arrays.sort(cnt);

        long output = 0;
        for (int i = n; i > 0 && cnt[i - 1] > 0; i--) {
            output += ((long) i * (long) cnt[i - 1]);
        }
        return output;
    }
}
