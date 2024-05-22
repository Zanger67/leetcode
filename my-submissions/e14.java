// https://leetcode.com/problems/longest-common-prefix/

class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs.length == 1) {
            return strs[0];
        }

        int shortestLen = strs[0].length();
        for (int i = 0; i < strs.length; i++) {
            shortestLen = Math.min(strs[i].length(), shortestLen);
        }

        for (int i = 0; i < shortestLen; i++) {
            for (int j = 1; j < strs.length; j++) {
                if (strs[j].charAt(i) != strs[j - 1].charAt(i)) {
                    return strs[0].substring(0,i);
                }
            }
        }

        return strs[0].substring(0, shortestLen);
    }
}