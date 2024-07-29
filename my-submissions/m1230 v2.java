class Solution {
    public double probabilityOfHeads(double[] prob, int target) {
        double[][] sols = new double[prob.length + 1][target + 1];
        sols[0][0] = 1;

        for (int r = 1; r < prob.length + 1; r++) {
            sols[r][0] = sols[r - 1][0] * (1 - prob[r - 1]);
            for (int c = 1; c < target + 1; c++) {
                sols[r][c] = sols[r - 1][c] * (1 - prob[r - 1])
                                + sols[r - 1][c - 1] * prob[r - 1];
            }
        }

        return sols[sols.length - 1][sols[0].length - 1];
    }
}