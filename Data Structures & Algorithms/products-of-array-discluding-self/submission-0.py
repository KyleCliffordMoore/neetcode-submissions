class Solution:

    def getPrefix(self, prefixList, index):
        return prefixList[index]

    def getPostfix(self, postfixList, index):
        return postfixList[index + 1]

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Prefix List
        prefixList = [1] # extra value to the left of it
        product = 1
        for i in range(len(nums)):
            product *= nums[i]
            prefixList.append(product)
        # print(prefixList)

        # postfix List
        product = 1
        postfixList = []
        for i in range(len(nums) - 1, -1, -1):
            product *= nums[i]
            postfixList.append(product)
        postfixList.reverse()
        postfixList.append(1)
        # print(postfixList)

        # Get prefix
        answer = []
        for i in range(len(nums)):
            product = self.getPrefix(prefixList, i) * self.getPostfix(postfixList, i)
            answer.append(product)

        return answer