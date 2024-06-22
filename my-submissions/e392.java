class Solution {
    public boolean isSubsequence(String s, String t) {
        if (s.length() == 0)
            return true;

        int sPointer = 0;
        
        for (int tPointer = 0; tPointer < t.length(); tPointer++) {
            if (s.charAt(sPointer) == t.charAt(tPointer)) {
                sPointer++;

                if (sPointer >= s.length())
                    return true;    
            }
        }
        return false;
    }
}