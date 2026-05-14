class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # initialize a results list
        # define a backtrack function
        # if the current fixed position is equal to the length of the list,
        # it means we finished building one permutation
        # for each position, choose which value should be fixed there
        # among the remaining values, try every possible choice

        res = []

        def backtrack(nums, index):

            # base case:
            # all positions are fixed, so we completed one permutation
            if index == len(nums):
                res.append(nums.copy())
                return

            # try every remaining number for the current position
            for i in range(index, len(nums)):

                # make the choice:
                # put nums[i] into the current fixed position
                nums[i], nums[index] = nums[index], nums[i]

                # recurse on the next position
                backtrack(nums, index + 1)

                # undo the choice:
                # restore the array before exploring the next branch
                nums[i], nums[index] = nums[index], nums[i]

        backtrack(nums, 0)
        return res

        # MAIN TAKEAWAYS

        # the index is also the depth of the decision tree.
        #
        # at the beginning, I choose which number goes into the first position
        #
        # at the second invocation, each branch already has
        # a different fixed first number in the permutation,
        # so I choose among the remaining numbers
        #
        # swapping is important because it places the chosen number
        # into the current fixed position while keeping the remaining
        # candidate numbers on the right side
        #
        # after recursion returns, we swap back
        # to restore the previous state before exploring another branch

        # REMEMBER:
        # backtracking usually follows this pattern:
        #
        # make a choice -> recurse -> undo the choice