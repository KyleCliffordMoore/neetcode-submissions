class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:

        def canSpell(word):
            freqs = Counter(word)

            for char in chars:
                if char not in freqs:
                    continue
                
                freqs[char] -= 1
                if freqs[char] <= 0:
                    del freqs[char]
            
            return len(freqs) == 0

        count = 0
        for word in words:
            if canSpell(word):
                count += len(word)
        return count

                