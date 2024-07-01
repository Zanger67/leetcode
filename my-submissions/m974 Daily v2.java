class Solution {
    public int subarraysDivByK(int[] nums, int k) {
        HashMap<Integer, Integer> pastRemainders = new HashMap<>();
        pastRemainders.put(0, 1);

        int runningRemainder = 0;
        int outputCounter = 0;

        for (Integer num : nums) {
            runningRemainder = (runningRemainder + (num % k) + k) % k;
            outputCounter += pastRemainders.getOrDefault(runningRemainder, 0);
            pastRemainders.put(runningRemainder, pastRemainders.getOrDefault(runningRemainder, 0) + 1);
        }

        return outputCounter;
        
    }

    
}