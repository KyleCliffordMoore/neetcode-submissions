class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) == 0:
            return []
        
        answer = [0] * len(temperatures)
        myStack = [[temperatures[0], 0]] # temp, index

        for i, temp in enumerate(temperatures):
            while len(myStack) > 0 and temp > myStack[-1][0]:
                j = myStack.pop()[1]
                numDays = i - j
                answer[j] = numDays
            myStack.append([temp, i])

        return answer