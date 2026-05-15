from functools import cache
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        @cache
        def isPali(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left+=1
                right-=1
                    
            return True

        def backtrack(subset, index):
            if index == len(s):
                res.append(subset.copy())

            for end in range(index, len(s)):
                if isPali(index, end):
                    subset.append(s[index:end+1])
                    backtrack(subset, end+1)
                    subset.pop()
        backtrack([], 0)
        return res
            


        #          aab
        #  a, ab    aa, b     aab
        #  return  a,a,b      return 

        
        