class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        charCount = [0] * 26
        
        for word in words:
            for char in word:
                charCount[ord(char) - ord('a')] += 1
        
        for num in charCount:
            if num % len(words) != 0:
                return False
        
        return True