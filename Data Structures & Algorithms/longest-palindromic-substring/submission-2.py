class Solution:
    def longestPalindrome(self, s: str) -> str:
        resIndex=0
        resLength=0

        for i in range(len(s)):
            left=right=i
            while left>=0 and right< len(s) and s[left]== s[right]:
                if right-left+1 > resLength:
                    resIndex=left
                    resLength=right-left+1
                
                left-=1
                right+=1

            left=i
            right=i+1
            while left>=0 and right<len(s) and s[left]==s[right]:
                if right-left+1>resLength:
                    resIndex=left
                    resLength=right-left+1

                left-=1
                right+=1
            
        return s[resIndex:resIndex+resLength]
                

        