class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        myStack = []
        operations = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: b - a,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(b / a)
        }
        for token in tokens:
            if token in operations:
               myStack.append(operations[token](myStack.pop(), myStack.pop()))
            else:
                myStack.append(int(token))
        return myStack[0]