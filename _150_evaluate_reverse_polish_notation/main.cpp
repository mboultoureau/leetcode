class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> stack;
        
        for (int i = 0; i < tokens.size(); i++) {
            // Token is a number
            if (tokens[i].size() > 1 || isdigit(tokens[i][0])) {
                stack.push(stoi(tokens[i]));
            } else {
                int b = stack.top();
                stack.pop();
                int a = stack.top();
                stack.pop();

                switch (tokens[i][0]) {
                    case '+':
                        stack.push(a + b);
                        break;
                    case '-':
                        stack.push(a - b);
                        break;
                    case '*':
                        stack.push(a * b);
                        break;
                    case '/':
                        stack.push(a / b);
                        break;
                }
            }
        }

        return stack.top();
    }
};