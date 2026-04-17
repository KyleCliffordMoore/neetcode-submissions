class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}

        for idx, num in enumerate(nums):
            diff = target - num
            if diff in visited:
                return [visited[diff], idx]
            else:
                visited[num] = idx