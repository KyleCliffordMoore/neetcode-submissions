class Solution:
    def largestGoodInteger(self, num: str) -> str:
        largest = -1

        for i in range(len(num) - 2):
            c1, c2, c3 = (num[i], num[i + 1], num[i + 2])

            if c1 == c2 and c2 == c3:
                largest = max(largest, int(c1 + c2 + c3))
        
        if largest < 0:
            return ""
        if largest == 0:
            return "000"
        return str(largest)