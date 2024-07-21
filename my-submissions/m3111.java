class Solution {
    public int minRectanglesToCoverPoints(int[][] points, int w) {
        int[] xVals = new int[points.length];
        for (int i = 0; i < points.length; i++) {
            xVals[i] = points[i][0];
        }

        Arrays.sort(xVals);

        int prev = w * -1 - 1;
        int counter = 0;

        for (int i : xVals) {
            if (i - prev > w) {
                prev = i;
                counter++;
            }
        }

        return counter;

    }
}