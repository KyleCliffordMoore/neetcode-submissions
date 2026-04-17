class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        myStack = []
        for token in tokens:
            if token == "*":
                val1 = myStack.pop()
                val2 = myStack.pop()
                myStack.append(val1 * val2)
            elif token == "+":
                val1 = myStack.pop()
                val2 = myStack.pop()
                myStack.append(val1 + val2)
            elif token == "-":
                val1 = myStack.pop()
                val2 = myStack.pop()
                myStack.append(val2 - val1)
            elif token == "/":
                val1 = myStack.pop()
                val2 = myStack.pop()
                myStack.append(int(val2 / val1))
            else:
                val = int(token)
                myStack.append(val)
        return myStack[0]