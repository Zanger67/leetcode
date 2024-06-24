class Solution {
    public List<List<Integer>> findWinners(int[][] matches) {
        HashMap<Integer, Integer> playerTracker = new HashMap<>();

        for (int[] i : matches) {
            playerTracker.put(i[0], playerTracker.getOrDefault(i[0], 0));       // winner
            playerTracker.put(i[1], playerTracker.getOrDefault(i[1], 0) + 1);   // loser
        }

        List<Integer> noLoss = new ArrayList<>();
        List<Integer> oneLoss = new ArrayList<>();
        for (Integer player : playerTracker.keySet()) {
            if (playerTracker.get(player) == 0) {
                noLoss.add(player);
            } else if (playerTracker.get(player) == 1) {
                oneLoss.add(player);
            }
        }

        Collections.sort(noLoss);
        Collections.sort(oneLoss);

        ArrayList<List<Integer>> output = new ArrayList<>();
        output.add((List<Integer>) noLoss);
        output.add((List<Integer>) oneLoss);

        return output;


    }
}