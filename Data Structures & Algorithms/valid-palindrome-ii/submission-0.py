class Solution:
    def validPalindrome(self, s: str) -> bool:

        def valid(string):
            l = 0
            r = len(string) - 1
            while l < r:
                if string[l] != string[r]:
                    return False
                r -= 1
                l += 1
            return True

        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                break
            left  += 1
            right -= 1
        
        if left >= right:
            return True
        
        return valid(s[left:right]) or valid(s[left + 1:right + 1])