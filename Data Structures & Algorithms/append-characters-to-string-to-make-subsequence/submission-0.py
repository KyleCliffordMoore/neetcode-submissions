class Solution:
    def appendCharacters(self, s: str, t: str) -> int:

        t_idx = 0
        for s_char in s:
            if s_char == t[t_idx]:
                t_idx += 1
                if t_idx == len(t):
                    return 0
        return len(t) - t_idx
        