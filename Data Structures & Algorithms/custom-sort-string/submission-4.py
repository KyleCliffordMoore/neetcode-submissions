class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        # ranks = [27] * 26
        # def toIdx(char):
        #     return ord(char) - ord('a')

        # for i in range(len(order)):
        #     ranks[toIdx(order[i])] = i
        
        # return "".join(sorted(s, key=lambda x: ranks[toIdx(x)]))

        counts = Counter(s)

        ans = ""
        for char in order:
            ans += char * counts[char]
            del counts[char]
        
        for char in counts:
            ans += char * counts[char]
        
        return ans