/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * public interface NestedInteger {
 *     // Constructor initializes an empty nested list.
 *     public NestedInteger();
 *
 *     // Constructor initializes a single integer.
 *     public NestedInteger(int value);
 *
 *     // @return true if this NestedInteger holds a single integer, rather than a nested list.
 *     public boolean isInteger();
 *
 *     // @return the single integer that this NestedInteger holds, if it holds a single integer
 *     // Return null if this NestedInteger holds a nested list
 *     public Integer getInteger();
 *
 *     // Set this NestedInteger to hold a single integer.
 *     public void setInteger(int value);
 *
 *     // Set this NestedInteger to hold a nested list and adds a nested integer to it.
 *     public void add(NestedInteger ni);
 *
 *     // @return the nested list that this NestedInteger holds, if it holds a nested list
 *     // Return empty list if this NestedInteger holds a single integer
 *     public List<NestedInteger> getList();
 * }
 */
class Solution {
    public int depthSumInverse(List<NestedInteger> nestedList) {
        int maxx = 1;
        int output = 0;

        Stack<Pair<Integer, Integer>> valsAndDepth = new Stack<>();
        Stack<Pair<NestedInteger, Integer>> toVisit = new Stack<>();
        
        for (NestedInteger i : nestedList)
            toVisit.add(new Pair(i, 1));
        
        while (!toVisit.isEmpty()){
            Pair<NestedInteger, Integer> curr = toVisit.pop();

            maxx = Integer.max(maxx, curr.getValue());
            if (curr.getKey().isInteger()) {
                valsAndDepth.push(new Pair(curr.getKey().getInteger(), curr.getValue()));
                continue;
            }

            for (NestedInteger i : curr.getKey().getList())
                toVisit.add(new Pair(i, curr.getValue() + 1));
        }

        while (!valsAndDepth.isEmpty()) {
            Pair<Integer, Integer> curr = valsAndDepth.pop();
            output += curr.getKey() * (maxx - curr.getValue() + 1);
        }

        return output;
    }
}