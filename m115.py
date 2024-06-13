# https://leetcode.com/problems/min-stack/description/

# Prompt: All operations must be O(1)

class MinStack {
    private Stack<int[]> vals;
    public MinStack() {
        this.vals = new Stack<>();
    }
    
    public void push(int val) {
        int newMin = (vals.size() > 0 && vals.peek()[1] < val) ? vals.peek()[1] : val;
        vals.push(new int[] {val, newMin});
    }
    
    public void pop() {
        vals.pop();
    }
    
    public int top() {
        return vals.peek()[0];
    }
    
    public int getMin() {
        return vals.peek()[1];
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */