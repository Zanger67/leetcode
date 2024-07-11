class FreqStack {
    private HashMap<Integer, Integer> _valFrequencyTracker;
    private Stack<Stack<Integer>> _frequencyValTracker;

    public FreqStack() {
        this._valFrequencyTracker = new HashMap<>();
        this._frequencyValTracker = new Stack<>();
    }
    
    public void push(int val) {
        _valFrequencyTracker.put(val, _valFrequencyTracker.getOrDefault(val, 0) + 1);

        if (_valFrequencyTracker.get(val) > _frequencyValTracker.size()) {
            _frequencyValTracker.push(new Stack<Integer>());
        }
        
        _frequencyValTracker.get(_valFrequencyTracker.get(val) - 1).push(val);
    }
    
    public int pop() {
        if (_frequencyValTracker.peek().isEmpty()) {
            _frequencyValTracker.pop();
        }

        int output = _frequencyValTracker.peek().pop();
        _valFrequencyTracker.put(output, _valFrequencyTracker.get(output) - 1);

        return output;
    }
}

/**
 * Your FreqStack object will be instantiated and called as such:
 * FreqStack obj = new FreqStack();
 * obj.push(val);
 * int param_2 = obj.pop();
 */