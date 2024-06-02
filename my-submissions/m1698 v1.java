// https://leetcode.com/problems/number-of-distinct-substrings-in-a-string/

// Same as v1 python just using Java

class Solution {
    private HashSet<String> visited = new HashSet<>();
    public int countDistinct(String s) {
        helper(s);
        return visited.size();
    }

    private void helper(String s) {
        if (visited.contains(s) || s.length() == 0) {
            return;
        }

        visited.add(s);
        helper(s.substring(1));
        helper(s.substring(0, s.length() - 1));
    }
}