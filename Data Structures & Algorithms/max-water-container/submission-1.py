class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0 
        right = len(heights)-1
        max_area = 0

        while left < right and right < len(heights):
            base = right-left
            height = min(heights[left],heights[right])
            current_area = base*height
            max_area = max(current_area, max_area)
            
            if heights[right] > heights[left]: 
                left+=1
            elif heights[right] < heights[left]:
                right-=1
            else:
                left+=1
                right-=1

        return max_area



        