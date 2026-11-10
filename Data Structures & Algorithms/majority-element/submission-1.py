class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = res = 0

        for num in nums:
            if counter == 0:
                res = num
            counter += (1 if num == res else -1)

        return res