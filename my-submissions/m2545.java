class Solution {
    public int[][] sortTheStudents(int[][] score, int k) {
        Arrays.sort(score, new Comparator<int[]>() {
            public int compare(int[] a, int[] b) {
                return -1 * Integer.compare(a[k], b[k]);
            }
        });

        return score;
    }
}