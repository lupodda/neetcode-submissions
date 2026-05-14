class Solution:
    def isPalindrome(self, s: str) -> bool:
        j = len(s)-1
        s = s.lower()

        for i in range(len(s)):
            
            if not s[i].isalnum():
                continue

            while not s[j].isalnum():
                j -= 1
                
            if s[i] == s[j]:
                if i == j:
                    return True
                j -= 1
                continue 
            else:
                return False

        return True