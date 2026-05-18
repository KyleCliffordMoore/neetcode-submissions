class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []

        for rock in asteroids:
            if rock < 0:
                while stack and -rock > stack[-1] and stack[-1] > 0:
                    stack.pop()
                if len(stack) > 0 and -rock == stack[-1]:
                    stack.pop()
                    continue
                if not stack or stack[-1] < 0:
                    stack.append(rock)
            else:
                stack.append(rock)

        return stack