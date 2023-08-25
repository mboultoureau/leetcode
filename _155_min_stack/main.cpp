class MinStack {
public:
    vector<int> stack;
    vector<int> minimuns;

    MinStack() {
        
    }
    
    void push(int val) {
        stack.push_back(val);

        if (stack.size() == 1) {
            minimuns.push_back(val);
        } else {
            minimuns.push_back(min(val, minimuns[minimuns.size() - 1]));
        }
    }
    
    void pop() {
        minimuns.pop_back();
        stack.pop_back();
    }
    
    int top() {
        return stack.back();
    }
    
    int getMin() {
        if (stack.size() == 0) {
            return 0;
        } else {
            return minimuns.back();
        }
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */