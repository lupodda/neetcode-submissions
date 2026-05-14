from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # retrun "" if t == ""
        # count the frequences in t and store them in freq_t
        # initialize need var with the number of unique chars in t
        # initialize have var with 0 (it is the number of unique char in window that match the freq in t)
        # count the freqences of in the current window
        # if have < need -> expand the window
        # while have == need -> shrink the window form left
        # update the maximum length of the window and the corresponting left and right pointer

        if t == "":
            return ""
        
        freq_t = Counter(t)
        freq_window = defaultdict(int)

        need = len(freq_t)
        have = 0
        res, res_len = [-1,-1], float("inf")

        left = 0
        
        for right in range(len(s)):
            right_char = s[right]
            freq_window[right_char] += 1

            if right_char in freq_t and freq_window[right_char] == freq_t[right_char]:
                have += 1
            
            while have == need:
                left_char = s[left]
                freq_window[left_char] -= 1

                if left_char in freq_t and freq_window[left_char] < freq_t[left_char]:
                    have -= 1

                if right-left+1 < res_len:
                    res_len = right-left+1
                    res = [left,right]

                left += 1

        left,right = res
        return s[left:right+1] if res_len != float("inf") else ""



        