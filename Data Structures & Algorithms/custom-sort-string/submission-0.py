class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        ranks = [float('inf')] * 26
        def toIdx(char):
            return ord(char) - ord('a')

        for i in range(len(order)):
            ranks[toIdx(order[i])] = i
        
        return "".join(sorted(s, key=lambda x: ranks[toIdx(x)]))

