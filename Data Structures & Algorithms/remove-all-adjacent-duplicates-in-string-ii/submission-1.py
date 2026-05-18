class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        stack = []

        for char in s:

            if len(stack) + 1 >= k:
                i = 1
                while i < k and stack[-i] == char:
                    i += 1
                if i == k: # All the same
                    # print(f"All same {char}")
                    i -= 1
                    del stack[-i:]
                    continue
            stack.append(char)
        return "".join(stack)
