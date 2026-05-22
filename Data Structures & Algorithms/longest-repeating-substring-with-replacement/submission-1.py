class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        characters = defaultdict(int)
        maxFreq = 0
        maxLen = 0
        left = 0

        for right in range(len(s)):

            characters[s[right]] += 1

            maxFreq = 0
            for char in characters:
                maxFreq = max(maxFreq, characters[char])

            while (right - left + 1) - maxFreq > k:
                characters[s[left]] -= 1
                left += 1

            maxLen = max(maxLen, right - left + 1)

        return maxLen