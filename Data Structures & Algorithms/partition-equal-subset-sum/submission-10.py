class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        if total%2 != 0:
            return False

        target = total // 2
        dp = set({0})

        for i in range(n):
            new_dp = set()
            for s in dp:
                if nums[i]+s == target:
                    return True
                new_dp.add(nums[i]+s)
                new_dp.add(s)
            
            dp = new_dp

        return False
        
