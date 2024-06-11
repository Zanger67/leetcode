// https://leetcode.com/problems/relative-sort-array/description/?envType=daily-question&envId=2024-06-11

class Solution {
    public int[] relativeSortArray(int[] arr1, int[] arr2) {
        HashSet<Integer> arr2vals = new HashSet<>();
        for (Integer i : arr2) {
            arr2vals.add(i);
        }

        HashMap<Integer, Integer> cnt = new HashMap<>();
        for (Integer i : arr1) {
            cnt.put(i, cnt.getOrDefault(i, 0) + 1);
        }


        int indx = 0;
        int[] output = new int[arr1.length];
        for (int i : arr2) {
            for (int j = 0; j < cnt.get(i); j++, indx++) {
                output[indx] = i;
            }
            cnt.remove(i);
        }
        
        int remainderIndx = 0;
        int[] remainingKeys = new int[cnt.size()];
        for (Integer i : cnt.keySet()) {
            remainingKeys[remainderIndx] = i;
            remainderIndx++;
        }
        Arrays.sort(remainingKeys);

        for (Integer i : remainingKeys) {
            for (int j = 0; j < cnt.get(i); j++, indx++) {
                output[indx] = i;
            }
        }

        return output;

    }
}