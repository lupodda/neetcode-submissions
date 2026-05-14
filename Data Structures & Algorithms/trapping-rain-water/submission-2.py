class Solution:
    def trap(self, height: List[int]) -> int:
        # start with two pointers, one at the beginning and one at the end
        # compute the current area as (r-l)*min(h[l], h[r])
        # update max_h if the new value is bigger
        # if h[l]>h[r]: r-=1
        # elif h[l]<h[r]:l+=1
        # else:l+=1 r+=1
        # return max_area
        n=len(height)
        l,r = 0,n-1
        max_area=0
        max_left,max_right=height[l],height[r]

        while l<r:
            if max_left < max_right:
                l+=1
                max_left=max(max_left,height[l])
                max_area+= max_left - height[l]
            else:
                r-=1
                max_right=max(max_right,height[r])
                max_area+= max_right-height[r]
        return max_area


    