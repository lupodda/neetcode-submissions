'''
At each digit, how many ways can I decode the string up to this point?
We'll define:
prev1 = number of ways to decode up to the previous character
prev2 = number of ways to decode up to two characters ago
'''
'''221'''
'''209'''
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        prev2, prev1 = 1,  1
        n = len(s)
        for i in range(1, n):
            curr = 0
            if s[i] != '0':
                curr += prev1
            if 10 <= int(s[i-1:i+1]) <= 26:
                curr += prev2
            prev2, prev1 = prev1, curr
        return prev1