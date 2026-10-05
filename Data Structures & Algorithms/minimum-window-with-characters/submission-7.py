from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq_t = Counter(t)
        freq_window = defaultdict(int)

        need = len(freq_t)
        have = 0

        start = end = 0
        min_window_length = float("inf")
        left = 0

        for right, c in enumerate(s):
            freq_window[c] += 1

            if c in freq_t and freq_window[c] == freq_t[c]:
                have +=1

            while have == need:
                if right-left+1 < min_window_length:
                    min_window_length = right-left+1
                    start = left
                    end = right
                    
                c_left = s[left]
                freq_window[c_left] -=1
                left +=1
                if c_left in freq_t and freq_window[c_left] < freq_t[c_left]:
                    have -= 1

        return s[start:end+1] if min_window_length < float("inf") else ""
                
