class Solution {
    public String customSortString(String order, String s) {
        HashMap<Character, Integer> reference = new HashMap<>();
        for (int i = 0; i < order.length(); i++) {
            reference.put(order.charAt(i), i);
        }

        Character[] output = new Character[s.length()];
        for (int i = 0; i < s.length(); i++) {
            output[i] = s.charAt(i);
        }

        Arrays.sort(output, (a, b) -> reference.getOrDefault(a, Integer.MAX_VALUE) - reference.getOrDefault(b, Integer.MAX_VALUE));

        StringBuilder sb = new StringBuilder();

        for (char c : output) {
            sb.append(c);
        }

        return sb.toString();
    }
}