class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        prefixSum = [0] * (len(nums) + 1)
        counts = defaultdict(int)
        counts[0] = 1

        summation = 0
        ans = 0
        for idx, num in enumerate(nums):
            summation += num

            if summation - k in counts:
                ans += counts[summation - k]
            
            counts[summation] += 1
            # print(counts)

        return ans