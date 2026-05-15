class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s) // 2):
            fordward_idx = i
            backward_idx = len(s) - 1 - i

            s[fordward_idx], s[backward_idx] = s[backward_idx], s[fordward_idx]
        