class Solution:
    def simplifyPath(self, path: str) -> str:

        stack = []

        for node in path.split("/"):
            if node == "." or node == "":
                continue
            elif node == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(node)
        
        return "/" + "/".join(stack)
