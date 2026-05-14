class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hash_s = {}  
        hash_t = {}

        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]
            if char_s not in hash_s:
                hash_s[char_s] = 1
            else:
                hash_s[char_s] += 1

            if char_t not in hash_t:
                hash_t[char_t] = 1
            else:
                hash_t[char_t] += 1

        return hash_s == hash_t
        

