from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if t == "":
            return ""

        freq_t = defaultdict(int)
        freq_window = defaultdict(int)
        
        for c in t:
            freq_t[c] += 1
        
        have, need = 0, len(freq_t) #len(freq_t) is the number of unique chars in t

        res, resLen  = [-1,-1], float("inf")

        left = 0 
        # Input: s = "OUZODYXAZV", t = "XYZ"
        # Output: "YXAZ"
        for right in range(len(s)):
            right_char = s[right]

            freq_window[right_char] += 1

            if right_char in freq_t and freq_window[right_char] == freq_t[right_char]:
                have += 1
            
            while have == need:
                if (right-left+1) < resLen:
                    res = [left, right]
                    resLen = right-left+1

                freq_window[s[left]] -= 1

                left_char = s[left]
                if left_char in freq_t and freq_window[left_char] < freq_t[left_char]:
                    have -= 1
                
                left += 1
        left, right = res

        return s[left:right+1] if resLen != float("inf") else ""


        
        
