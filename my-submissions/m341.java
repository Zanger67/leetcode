/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * public interface NestedInteger {
 *
 *     // @return true if this NestedInteger holds a single integer, rather than a nested list.
 *     public boolean isInteger();
 *
 *     // @return the single integer that this NestedInteger holds, if it holds a single integer
 *     // Return null if this NestedInteger holds a nested list
 *     public Integer getInteger();
 *
 *     // @return the nested list that this NestedInteger holds, if it holds a nested list
 *     // Return empty list if this NestedInteger holds a single integer
 *     public List<NestedInteger> getList();
 * }
 */
public class NestedIterator implements Iterator<Integer> {
    private List<NestedInteger> data;
    private dataManagement manager;
    public NestedIterator(List<NestedInteger> nestedList) {
        this.data = nestedList;


        // Parses data upon receiving it, recursively removing any
        // cases that are empty i.e. containing no integer values
        for (int i = data.size() - 1; i >= 0; i--) {
            if (isEmpty(data.get(i))) {
                data.remove(i);
            }
        }

        // Assigns a managing private inner class so that the 
        // recusive creations of "NestedIterators" don't revalidate
        // the data (checking and removing empty sub-NestedIntegers)
        this.manager = new dataManagement(nestedList);
    }

    private boolean isEmpty(NestedInteger curr) {
        if (curr == null) {
            return true;
        }
        if (curr.isInteger()) {
            return false;
        }
        for (int i = curr.getList().size() - 1; i >= 0; i--) {
            if (isEmpty(curr.getList().get(i))) {
                curr.getList().remove(i);
            }
        }
        return curr.getList().size() == 0;
    }

    @Override
    public Integer next() {
        return manager.next();
    }

    @Override
    public boolean hasNext() {
        return manager.hasNext();
    }

    private class dataManagement{
        private List<NestedInteger> data;
        private dataManagement curr;
        public dataManagement(List<NestedInteger> nestedList) {
            this.data = nestedList;
        }

        public Integer next() {
            if (curr != null) {
                Integer output = curr.next();
                if (!curr.hasNext()) {
                    curr = null;
                }
                return output;
            }

            if (data.get(0).isInteger()) {
                Integer output = data.get(0).getInteger();
                data.remove(0);
                return output;
            }

            curr = new dataManagement(data.get(0).getList());
            data.remove(0);
            return this.next();
        }

        public boolean hasNext() {
            if ((data.size() == 0) && (curr == null))
                return false;
            return true;
        }
    }
}

/**
 * Your NestedIterator object will be instantiated and called as such:
 * NestedIterator i = new NestedIterator(nestedList);
 * while (i.hasNext()) v[f()] = i.next();
 */