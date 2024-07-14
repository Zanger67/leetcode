class Solution {
    private List<String> output;
    private HashMap<Character, String> opts;
    private String digits;
    private StringBuilder sb;
    public List<String> letterCombinations(String digits) {
        this.output = new ArrayList<>();
        this.opts = new HashMap<>();
        this.sb = new StringBuilder();
        this.digits = digits;
        
        this.opts.put('2', "abc");
        this.opts.put('3', "def");
        this.opts.put('4', "ghi");
        this.opts.put('5', "jkl");
        this.opts.put('6', "mno");
        this.opts.put('7', "pqrs");
        this.opts.put('8', "tuv");
        this.opts.put('9', "wxyz");

        helper(0);
        return output;
    }

    private void helper(int curr) {
        if (curr >= digits.length()) {
            if (sb.length() > 0) {
                output.add(sb.toString());
            }
            return;
        }

        for (char c : opts.get(digits.charAt(curr)).toCharArray()) {
            sb.append(c);
            helper(curr + 1);
            sb.deleteCharAt(sb.length() - 1);
        }
    }
}