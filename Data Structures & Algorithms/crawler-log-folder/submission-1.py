class Solution:
    def minOperations(self, logs: List[str]) -> int:
        
        stack = 0
        for log in logs:
            if log == "./":
                continue
            elif log == "../":
                stack = max(stack - 1, 0)
            else:
                stack += 1
        return stack