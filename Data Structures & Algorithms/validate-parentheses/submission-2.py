class Solution:

    def isValid(self, s: str) -> bool:
        
        stack = []

        def isOpen(p):
            return p in ['[', '(', '{']

        def isMatch(p1, p2):
            return (
                p1 == '{' and p2 == '}' or
                p1 == '[' and p2 == ']' or
                p1 == '(' and p2 == ')'
            )

        for para in s:

            # Open Case
            if isOpen(para):
                stack.append(para)
                continue
            
            # Close Case
            if not stack or not isMatch(stack.pop(), para):
                return False
        
        return not stack