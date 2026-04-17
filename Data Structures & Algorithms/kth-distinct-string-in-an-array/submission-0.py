class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freqs = Counter(arr)

        for word in arr:
            if freqs[word] == 1:
                k -= 1
                if k <= 0:
                    return word
        
        return ""