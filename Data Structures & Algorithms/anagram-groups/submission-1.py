class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def toIdx(char):
            return ord(char) - ord('a')

        anagrams = defaultdict(list)

        for string in strs:
            arr = [0] * 26

            for char in string:
                arr[toIdx(char)] += 1
            
            anagrams[tuple(arr)].append(string)
            
        
        return list(anagrams.values())