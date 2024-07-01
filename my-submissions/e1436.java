class Solution {
    public String destCity(List<List<String>> paths) {
        HashSet<String> srcs = new HashSet<>();

        for (int i = 0; i < paths.size(); i++) {
            srcs.add(paths.get(i).get(0));
        }

        for (int i = 0; i < paths.size(); i++) {
            if (!srcs.contains(paths.get(i).get(1))) {
                return paths.get(i).get(1);
            }
        }
        return null;
    }
}