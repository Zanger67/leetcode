class RandomizedCollection {

    private ArrayList<Integer> vals;
    private HashMap<Integer, HashSet<Integer>> indices;
    public RandomizedCollection() {
        this.vals = new ArrayList<>();
        this.indices = new HashMap<>();
    }
    
    public boolean insert(int val) {
        if (!this.indices.containsKey(val)) {
            this.indices.put(val, new HashSet<>());
        }
        this.indices.get(val).add(this.vals.size());
        this.vals.add(val);

        // If it wasn't present before, the new size will be 1
        return this.indices.get(val).size() <= 1;
    }
    
    public boolean remove(int val) {
        if (!this.indices.containsKey(val)) {
            return false;
        }

        int indx = this.indices.get(val).iterator().next();
        this.indices.get(val).remove(indx);

        if (indx == vals.size() - 1) {
            this.vals.removeLast();
        } else {
            int lastVal = this.vals.removeLast();
            this.vals.set(indx, lastVal);
            this.indices.get(lastVal).remove(this.vals.size());
            this.indices.get(lastVal).add(indx);
        }
        // Cleanup
        if (this.indices.get(val).size() == 0) {
            this.indices.remove(val);
        }
        return true;
    }
    
    public int getRandom() {
        return this.vals.get((int) (Math.random() * this.vals.size()));
    }
}

/**
 * Your RandomizedCollection object will be instantiated and called as such:
 * RandomizedCollection obj = new RandomizedCollection();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */