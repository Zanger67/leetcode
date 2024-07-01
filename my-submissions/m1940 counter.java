// weekly premium question

class Solution {
    public List<Integer> longestCommonSubsequence(int[][] arrays) {
        HashMap<Integer, Integer> counter = new HashMap<>();

        for (int[] subArr: arrays){
            for (int i: subArr) {
                counter.put(i, counter.getOrDefault(i, 0) + 1);
            }
        }

        ArrayList<Integer> output = new ArrayList<>();
        
        for (int i: counter.keySet()) {
            if (counter.getOrDefault(i, 0) == arrays.length) {
                output.add(i);
            }
        }
        Collections.sort(output);

        return output;
    }
}