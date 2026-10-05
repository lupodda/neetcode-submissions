class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0]=="0":
            return 0

        prev=prev_prev=1
        n=len(s)
        for i in range(1, n):
            curr=0
            if s[i]!="0":
                curr+=prev
            
            if 10<= int(s[i-1:i+1])<=26:
                curr+=prev_prev
            
            prev_prev, prev=prev, curr

        return prev

        
        