class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        
        converted_to_happy = 0
        for i in range(minutes):
            if grumpy[i] == 1: # He is usually unhappy
                converted_to_happy += customers[i]
        
        max_converted_to_happy = converted_to_happy

        for i in range(minutes, len(customers)):
            if grumpy[i] == 1:
                converted_to_happy += customers[i]
            if grumpy[i - minutes] == 1:
                converted_to_happy -= customers[i - minutes]
            max_converted_to_happy = max(max_converted_to_happy, converted_to_happy)
        
        total = sum([ (customers[i] if grumpy[i] == 0 else 0) for i in range(len(customers))])
        total += max_converted_to_happy

        return total