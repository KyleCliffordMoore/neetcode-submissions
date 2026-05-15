class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        cleanedString = ""
        for char in s:
            if char.isalnum() or char.isdigit():
                cleanedString += char.lower()

        return cleanedString == cleanedString[::-1]