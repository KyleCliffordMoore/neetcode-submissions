class Solution:
    def calculate(self, s: str) -> int:
        


        stack = []
        last_op = "+"
        idx = 0
        operations = {
            "+": lambda num: stack.append(num),
            "-": lambda num: stack.append(-num),
            "*": lambda num: stack.append(stack.pop() * num),
            "/": lambda num: stack.append(int(stack.pop() / num)),
            None: lambda num: print("Well this is awkward", stack, idx)
        }
        while idx < len(s):
            if s[idx].isdigit():
                val = int(s[idx])
                end = idx + 1
                while end < len(s) and s[end].isdigit():
                    val = val * 10 + int(s[end])
                    end += 1
                
                # handle operation
                operations[last_op](val)

                last_op = None
            elif s[idx] != " ":
                last_op = s[idx]

            idx += 1
        print(stack)
        return sum(stack)

