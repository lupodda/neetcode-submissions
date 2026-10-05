class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0]=="0":
            return 0
        prev=prev2=1

        for i in range(1, len(s)):
            curr=0
            if s[i]!="0":
                curr+=prev
            if 10<=int(s[i-1:i+1])<=26:
                curr+=prev2
            
            prev2, prev= prev, curr

        return prev

        