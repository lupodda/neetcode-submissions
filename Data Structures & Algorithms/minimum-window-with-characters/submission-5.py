from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Initialization: left pointer for the window; 
        #                 need, have to see how many letter's freq match; 
        #                 start, end to save the indexed of a valid substring
        #                 min_substring_length = inf
        # ds initialization: count frequencies for t and initialize default dict for the frewuncies in the current window
        # start expanding at each step the corrent window with enumerate s
        # update the frequencies of s
        # increase the have value if char is in t and freq_s = freq_t 
        # start a while have = need
        # if right-left+1 (the current window) < substring_length:
        #    updates start, end
        #    update substring_length
        # 
        # decrement the freq_s of the left char
        # if c in t and freq_s[c] < freq_t[c]: if i have removed a char in t
        #       have-=1
        # left+=1

        freq_t = Counter(t)
        freq_window = defaultdict(int)

        left = 0
        need = len(freq_t)
        have = 0
        min_window_length = float("inf")
        start = end = 0

        for right, c in enumerate(s):
            freq_window[c] += 1
            if c in freq_t and freq_window[c] == freq_t[c]:
                have += 1
            
            while need == have:
                if right-left+1 < min_window_length:
                    start = left
                    end = right
                    min_window_length = end-start+1

                c_left = s[left]
                freq_window[c_left] -= 1
                if c_left in freq_t and freq_window[c_left] < freq_t[c_left]:
                    have -= 1
                left += 1

        return s[start:end+1] if min_window_length < float("inf") else ""





        