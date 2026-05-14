class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def can_eat_all_bananas(eating_rate):
            needed_hours = 0
            for pile in piles:
                needed_hours += math.ceil(pile/eating_rate)
            return needed_hours <= h

        left = 1
        right = max(piles)
        while left < right:
            eating_rate = (left+right)//2
            if can_eat_all_bananas(eating_rate):
                right = eating_rate
            else:
                left = eating_rate+1
                
        return left
        