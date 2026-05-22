class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        idx = lambda char: ord(char) - ord('a')

        S1_ARR      = [0] * 26
        curr_window = [0] * 26
        for char1, char2 in zip(s1, s2[:len(s1)]):
            S1_ARR[idx(char1)]      += 1
            curr_window[idx(char2)] += 1
        
        if curr_window == S1_ARR:
            return True
        
        for incoming, outgoing in zip(s2[len(s1):], s2):
            curr_window[idx(incoming)] += 1
            curr_window[idx(outgoing)] -= 1

            if curr_window == S1_ARR:
                return True
        
        return False