class Solution:
    def partition(self, s: str) -> List[List[str]]:

        #            aab
        #      /           \
        #   a,ab           aab
        #   /   \         /    \
        #a,a,b  a,ab   aa,b     aab

        res = []
        def isPalindrome(left, right):
         # a,  ab
            while left <right:
                if s[left] == s[right]:
                    left+=1
                    right-=1
                else:
                    return False

            return True

        def backtrack(subset, index):
            # if split is at the end of s we append subset to res

            if index == len(s):
                res.append(subset.copy())
                return

            for end in range(index, len(s)):
                
                if isPalindrome(index, end):
                    subset.append(s[index:end+1])
                    backtrack(subset, end+1)
                    subset.pop()

        backtrack([], 0)
        return res

