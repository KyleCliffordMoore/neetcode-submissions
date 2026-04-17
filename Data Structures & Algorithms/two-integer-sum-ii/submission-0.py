class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numDict = {}
        for index, number in enumerate(numbers):
            numDict[number] = index + 1
        
        for key in numDict:
            if target - key in numDict:
                return [numDict[key], numDict[target - key]]

        return []