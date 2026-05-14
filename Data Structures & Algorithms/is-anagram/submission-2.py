class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        freqS = [0]*26
        freqT = [0]*26

        for i in range(len(s)):
            freqS[ord(s[i])-ord("a")]+=1
            freqT[ord(t[i])-ord("a")]+=1

        for i in range(26):
            if freqS[i] != freqT[i]:
                return False
        return True

        