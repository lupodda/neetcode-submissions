class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            res += self.count_pali(s, i, i)
            res += self.count_pali(s, i, i+1)

        return res
    def count_pali(self, s, left, right):
        res = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            res += 1
            left -=1
            right +=1

        return res

