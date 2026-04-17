class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()

        ans = []
        curr = []

        def backtrack(idx, currSum):
            if target - currSum == 0:
                ans.append(curr.copy())
            if target - currSum < 0:
                return
            
            last = -99999
            for i in range(idx, len(candidates)):
                if candidates[i] == last:
                    continue
                curr.append(candidates[i])
                backtrack(i + 1, currSum + candidates[i])
                last = curr.pop()

        backtrack(0, 0)
        return ans