class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magFreqs = Counter(magazine)

        for char in ransomNote:
            if char not in magFreqs:
                return False
            
            magFreqs[char] -= 1
            if magFreqs[char] < 0:
                return False
        
        return True