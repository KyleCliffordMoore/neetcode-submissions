class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        char_to_word = {}
        word_to_char = {}

        if len(pattern) != len(words):
            return False
        
        for i in range(len(pattern)):
            char = pattern[i]
            word = words[i]

            if char not in char_to_word and word not in word_to_char:
                char_to_word[char] = word
                word_to_char[word] = char

            else:
                if char_to_word.get(char) != word or word_to_char.get(word) != char:
                    return False
        
        return True
