class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        
        word_idx = 0
        abbr_idx = 0
        while word_idx < len(word):

            if word[word_idx] == abbr[abbr_idx]:
                word_idx += 1
                abbr_idx += 1
            else:

                if not abbr[abbr_idx].isnumeric() or int(abbr[abbr_idx]) == 0:
                    return False

                num = 0
                i = abbr_idx
                while i < len(abbr):
                    if not abbr[i].isnumeric():
                        break
                    num = num * 10 + int(abbr[i])
                    i += 1
                word_idx += num
                abbr_idx = i

        return word_idx == len(word) and abbr_idx == len(abbr)