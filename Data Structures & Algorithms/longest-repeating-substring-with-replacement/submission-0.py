class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        characters = {}
        maxFreq = 0
        maxLen = 0
        left = 0

        for right in range(len(s)):

            characters[s[right]] = characters.get(s[right], 0) + 1

            maxFreq = max(maxFreq, characters[s[right]])

            for char in characters:
                while (right - left + 1) - maxFreq > k:
                    characters[s[left]] -= 1
                    left += 1

            maxLen = max(maxLen, right - left + 1)

        return maxLen