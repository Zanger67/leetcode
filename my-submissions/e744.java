class Solution {
    public char nextGreatestLetter(char[] letters, char target) {
        int left = 0;
        int right = letters.length - 1;


        while (left < right) {
            int mid = (left + right) / 2;
            
            if (letters[mid] <= target) {
                left = mid + 1;
                continue;
            }

            right = mid - 1;
        }
        
        if (letters[left] <= target)
            return letters[(left + 1) % letters.length];
        return letters[left];
    }
}