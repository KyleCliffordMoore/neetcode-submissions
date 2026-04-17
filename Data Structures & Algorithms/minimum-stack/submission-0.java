class MinStack {

    ArrayList<Integer> stack;

    public MinStack() {
        stack = new ArrayList<Integer>();
    }
    
    public void push(int val) {
        stack.add(val);
    }
    
    public void pop() {
        stack.remove(stack.size() - 1);
    }
    
    public int top() {
        return stack.get(stack.size() - 1);
    }
    
    public int getMin() {
        int least = stack.get(0);
        for (int i : stack) {
            if (i < least) {
                least = i;
            }
        }
        return least;
    }
}
