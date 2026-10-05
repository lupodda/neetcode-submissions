class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)

        if total %2 != 0:
            return False

        target = total //2
        dp = set({0})

        for i in range(n):
            new_dp = set()
            print(dp)
            for t in dp: # dp stores all possible sum
                print(t)
                if nums[i]+t == target:
                    return True
                elif nums[i]+t < target:
                    new_dp.add(nums[i]+t)
                new_dp.add(t)
            dp = new_dp

        return False
        