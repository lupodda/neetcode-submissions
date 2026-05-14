class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left =0
        right=len(numbers)-1

        while left<right:
            possible_target=numbers[left]+numbers[right]
            if possible_target>target:
                right-=1
            elif possible_target<target:
                left+=1
            else:
                return [left+1,right+1]


        