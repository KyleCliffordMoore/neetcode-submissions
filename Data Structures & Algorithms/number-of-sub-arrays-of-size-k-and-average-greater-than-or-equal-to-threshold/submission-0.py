class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        threshold *= k

        currSum = sum(arr[:k])
        count = int(currSum >= threshold)

        for i in range(k, len(arr)):
            currSum -= arr[i - k]
            currSum += arr[i]

            count += int(currSum >= threshold)
        
        return count