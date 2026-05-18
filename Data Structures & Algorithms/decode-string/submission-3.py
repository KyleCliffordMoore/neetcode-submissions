class Solution:
    def decodeString(self, s: str) -> str:
        stack = [ [1, ""]]

        idx = 0
        while idx < len(s):
            char = s[idx]
            idx += 1

            if char.isnumeric():
                off = 0
                while idx - 1 + off < len(s) and s[idx - 1 + off].isnumeric():
                    off += 1
                char = s[idx - 1:idx - 1 + off]
                idx += off

                stack.append( [int(char), ""] )
                continue
            if char == "[":
                continue
            if char == "]":
                times, msg = stack.pop()
                stack[-1][1] += msg * times
                continue

            stack[-1][1] += char
        
        return stack[0][1]