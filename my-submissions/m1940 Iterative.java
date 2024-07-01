// weekly premium question

// Interesting how for java, this solution with iterating is MUCH faster than the
// HashMap Counter method. But with Python, both the Counter and Set methods are
// MUCH faster than this iterative approach. I wonder why....

class Solution {
    public List<Integer> longestCommonSubsequence(int[][] arrays) {
        ArrayList<Integer> output = new ArrayList<>();

        int[] pointers = new int[arrays.length];
        int pointerForPointers = 0;

        int counter = 0;
        int currentMaxValue = Integer.MIN_VALUE;

        while (arrays[pointerForPointers].length > pointers[pointerForPointers]) {
            if (arrays[pointerForPointers][pointers[pointerForPointers]] < currentMaxValue) {
                pointers[pointerForPointers] += 1;
                continue;
            }

            // if (arrays[pointerForPointers][pointers[pointerForPointers]] > currentMaxValue) {
            currentMaxValue = arrays[pointerForPointers][pointers[pointerForPointers]];
            pointerForPointers = (pointerForPointers + 1) % pointers.length;
            counter = 1;
            continue;
            // }

            counter += 1;
            pointers[pointerForPointers] += 1;
            pointerForPointers = (pointerForPointers + 1) % pointers.length;

            if (counter == pointers.length) {
                output.add(currentMaxValue);
                currentMaxValue = arrays[pointerForPointers][pointers[pointerForPointers]];
                counter = 0;
            }
        }

        return output;

    }
}