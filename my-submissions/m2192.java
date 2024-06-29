class Solution {
    public List<List<Integer>> getAncestors(int n, int[][] edges) {
        ArrayList<HashSet<Integer>> parents = new ArrayList<>();
        
        for (int i = 0; i < n; i++) {
            parents.add(new HashSet<Integer>());
        }

        boolean[] visited = new boolean[n];

        for (int[] edge : edges) {
            parents.get(edge[1]).add(edge[0]);
        }

        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                helper(i, visited, parents);
            }
        }

        List<List<Integer>> output = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            output.add(new ArrayList<Integer>());
            output.get(i).addAll(parents.get(i));
            Collections.sort(output.get(i));
        }

        return output;

    }
    
    private void helper(int currentIndx, boolean[] visited, ArrayList<HashSet<Integer>> parents) {
        if (visited[currentIndx]) {
            return;
        }

        visited[currentIndx] = true;
        if (parents.get(currentIndx).size() == 0) {
            return;
        }

        HashSet<Integer> mergeValues = new HashSet<>();
        for (Integer i : parents.get(currentIndx)) {
            helper(i, visited, parents);
            mergeValues.addAll(parents.get(i));
        }
        parents.get(currentIndx).addAll(mergeValues);
     }

}
