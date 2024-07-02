/*
// Definition for Employee.
class Employee {
    public int id;
    public int importance;
    public List<Integer> subordinates;
};
*/

class Solution {
    public int getImportance(List<Employee> employees, int id) {
        HashMap<Integer, Pair<Integer, List<Integer>>> hs = new HashMap<>();
        for (Employee e : employees) {
            hs.put(e.id, new Pair<Integer, List<Integer>>(e.importance, e.subordinates));
        }

        return helper(id, hs);
    }

    private int helper(int id, HashMap<Integer, Pair<Integer, List<Integer>>> data) {
        int output = data.get(id).getKey();
        for (Integer i : data.get(id).getValue()) {
            output += helper(i, data);
        }
        return output;
    }
}