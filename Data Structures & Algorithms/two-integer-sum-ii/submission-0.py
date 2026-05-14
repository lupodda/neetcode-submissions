class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # we have to use the property of the array beeing sorted
        # Use two pointsrs, one from the beginning and one from the end
        # Until left < right
        # if n[l]+n[r]>t: r-=1
        # if n[l]+n[r]<t: l+=1
        # if n[l]+n[r]==t: return [l,r]
        n=len(numbers)
        l,r=0,n-1

        while l<r:
            if numbers[l]+numbers[r]>target:
                r-=1
            elif numbers[l]+numbers[r]<target:
                l+=1
            else:
                return [l+1,r+1]
        