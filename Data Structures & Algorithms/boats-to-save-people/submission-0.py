class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        left = 0
        right = len(people) - 1

        numBoats = 0

        print(people)

        while left < right:

            if people[left] + people[right] <= limit:
                numBoats += 1
                left += 1
                right -= 1
            else:
                if people[right] <= limit:
                    numBoats += 1
                right -= 1

        if left == right and people[left] <= limit:
            numBoats += 1

        return numBoats