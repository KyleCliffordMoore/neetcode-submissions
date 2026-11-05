class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        
        unordered_map<string, function<int(int, int)>> evalOp = {
            {"+", [](int a, int b) { return b + a; }},
            {"-", [](int a, int b) { return b - a; }},
            {"*", [](int a, int b) { return b * a; }},
            {"/", [](int a, int b) { return b / a; }},
        };

        stack<int> valuesStack;

        for (string token : tokens) {

            // token is a value
            if (evalOp.find(token) == evalOp.end()) {
                valuesStack.push(stoi(token));
                continue;
            }
                
            // token is an operation
            int a = valuesStack.top();
            valuesStack.pop();

            int b = valuesStack.top();
            valuesStack.pop();

            valuesStack.push(evalOp[token](a, b));

            // std::cout << "Operation: " << token << '\n';
            // std::cout << "Stack Top: " << valuesStack.top() << '\n';
        }

        return valuesStack.top();

    }
};
