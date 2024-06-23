class Solution {
    public int maxIceCream(int[] costs, int coins) {
        Arrays.sort(costs);

        for (int i = 0; i < costs.length; i++) {
            if (coins < costs[i]) 
                return i;
            coins -= costs[i];
        }

        return costs.length;
    }
}