class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0 
        right = len(heights)-1
        max_area = 0

        while left < right:
            base = right-left
            height = min(heights[left],heights[right])
            current_area = base*height
            max_area = max(current_area, max_area)
            
            # if heights[right] >= heights[left]: 
            #     left+=1
            # else:
            #     right-=1

            if heights[left] >= heights[right]: 
                right-=1
            else:
                left+=1
        return max_area



        