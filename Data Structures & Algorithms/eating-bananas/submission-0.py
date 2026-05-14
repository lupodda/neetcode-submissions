class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def eat_all_bananas(eating_speed):
            current_hours = 0
            for bananas in piles:
                current_hours += math.ceil(bananas/eating_speed)
            return current_hours <= h

        left, right = 1, max(piles)

        while left < right:
            eating_speed = (left +right) //2

            if eat_all_bananas(eating_speed):
                right = eating_speed
            else:
                left = eating_speed+1

        return left
        