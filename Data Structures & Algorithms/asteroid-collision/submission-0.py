class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # I loop over the asteroids array
        # I check the direction of the last element in the stack and of the current element
        # while these directions are opposite i pop for the stack
        # I check the conditions for the size of the asteroids and i push back the elements
        # I return the stack at the end
        stack = []
        for asteroid in asteroids:
            exploaded = False
            while stack and stack[-1] > 0 and asteroid < 0:
                if abs(stack[-1]) < abs(asteroid):
                    stack.pop()
                elif abs(stack[-1]) == abs(asteroid):
                    stack.pop()
                    exploaded = True
                    break
                else:
                    exploaded = True
                    break

            if not exploaded:
                stack.append(asteroid)

        return stack



