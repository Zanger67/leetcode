class RandomizedSet {
    private ArrayList<Integer> vals;
    private HashMap<Integer, Integer> indices;
    public RandomizedSet() {
        this.vals = new ArrayList<>();
        this.indices = new HashMap<>();
        
    }
    
    public boolean insert(int val) {
        if (this.indices.containsKey(val)) {
            return false;
        }
        this.indices.put(val, this.vals.size());
        this.vals.add(val);
        return true;
    }
    
    public boolean remove(int val) {
        if (!this.indices.containsKey(val)) {
            return false;
        }

        int indx = this.indices.remove(val);
        if (indx == vals.size() - 1) {
            this.vals.removeLast();
        } else {
            int lastVal = this.vals.removeLast();
            this.vals.set(indx, lastVal);
            this.indices.put(lastVal, indx);
        }
        return true;
    }
    
    public int getRandom() {
        return this.vals.get((int) (Math.random() * this.vals.size()));
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */