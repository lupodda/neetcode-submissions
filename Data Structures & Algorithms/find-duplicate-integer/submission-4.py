class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = slow = 0

        while True: # this is fine beacuse a duplicate is always guaranteed
            fast = nums[nums[fast]]
            slow = nums[slow]

            if fast == slow:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2:
                return slow
        return -1
            
        