class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.memo = {}
        self.cost = cost
        return min(self._minCost(0), self._minCost(1))
    
    def _minCost(self, index):
        if index >= len(self.cost):
            return 0

        if index in self.memo:
            return self.memo[index]

        self.memo[index] = self.cost[index]+min(self._minCost(index+1), self._minCost(index+2))

        return self.memo[index]
        