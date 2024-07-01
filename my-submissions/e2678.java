class Solution {
    public int countSeniors(String[] details) {
        int counter = 0;
        for (String str : details) {
            if (Integer.parseInt(str.substring(11,13)) > 60) {
                counter++;
            }
        }
        return counter;
    }
}