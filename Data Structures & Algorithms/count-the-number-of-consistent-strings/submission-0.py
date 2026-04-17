class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowSet = set(allowed)

        count = 0
        for word in words:
            passed = True
            for char in word:
                if char not in allowSet:
                    passed = False
                    continue
            
            if passed:
                count += 1
        
        return count