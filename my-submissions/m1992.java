class Solution {
    public int[][] findFarmland(int[][] land) {
        ArrayList<int[]> output = new ArrayList<>();

        for (int r = 0; r < land.length; r++) {
            for (int c = 0; c < land[0].length; c++) {
                if (land[r][c] == 1                         // Corner found
                    && (r == 0 || land[r - 1][c] == 0)
                    && (c == 0 || land[r][c - 1] == 0)) {
                    int[] group = new int[4];
                    group[0] = r;
                    group[1] = c;

                    for (int i = r + 1;; i++) {
                        if (i >= land.length || land[i][c] == 0) {
                            group[2] = i - 1;
                            break;
                        }
                    }
                    for (int i = c + 1;; i++) {
                        if (i >= land[0].length || land[r][i] == 0) {
                            group[3] = i - 1;
                            break;
                        }
                    }

                    output.add(group);
                }
            }
        }

        int[][] actualOutput = new int[output.size()][];
        for (int i = 0; i < output.size(); i++) {
            actualOutput[i] = output.get(i);
        }

        return actualOutput;
    }
}