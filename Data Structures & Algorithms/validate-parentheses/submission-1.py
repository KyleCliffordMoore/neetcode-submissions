class Solution:

    def isOpen(self, para):
        return para in {'(', '{', '['}

    def isMatch(self, open_, closed_):
        if open_ == '(' and closed_ == ')':
            return True
        if open_ == '{' and closed_ == '}':
            return True
        if open_ == '[' and closed_ == ']':
            return True
        return False

    def isValid(self, s: str) -> bool:
        paraStack = []
        
        for char in s:
            if self.isOpen(char):
                paraStack.append(char)
                continue
            
            if len(paraStack) == 0:
                return False
            
            if not self.isMatch(paraStack.pop(), char):
                return False

        return len(paraStack) == 0