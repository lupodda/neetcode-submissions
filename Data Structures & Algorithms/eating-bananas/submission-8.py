class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = sum(piles)

        def can_eat_all_bananas(eating_rate):
            current_time = 0
            for pile in piles:
                current_time += math.ceil(pile/eating_rate)

            return current_time <= h

        while left < right:
            eating_rate = (left+right) // 2
            if can_eat_all_bananas(eating_rate):
                right = eating_rate
            else:
                left = eating_rate+1

        return right


        