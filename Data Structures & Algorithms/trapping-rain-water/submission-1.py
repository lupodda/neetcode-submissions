class Solution:
    def trap(self, height: List[int]) -> int:
        # From the image, we can see that to calculate the amount of
        # water trapped at a position, the greater element to the left l 
        # and the greater element to the right r of the current position
        #  are crucial. The formula for the trapped water at index i is 
        #  given by: min(height[l], height[r]) - height[i].

        max_left = 0 
        max_right = 0 

        left = 0
        right = len(height)-1
        max_area = 0

        while left < right:   
            if height[left] < height[right]:
                if max_left < height[left]:
                    max_left = height[left]

                else:
                    max_area += max_left - height[left]
                left+=1
            else:
                if max_right < height[right]:
                    max_right = height[right]
                else:
                    max_area += max_right - height[right]
                right-=1
        return max_area 


