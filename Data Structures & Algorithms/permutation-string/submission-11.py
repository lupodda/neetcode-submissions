from collections import Counter, defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)> len(s2):
            return False
            
        left = 0
        right = len(s1)
        freq_s1 = Counter(s1)
        freq_window = Counter(s2[left:right])

        while right < len(s2):
            if freq_s1 == freq_window:
                return True
            
            freq_window[s2[left]] -= 1

            if freq_window[s2[left]] == 0:
                del freq_window[s2[left]]
                
            freq_window[s2[right]]+= 1

            left += 1
            right+= 1

        return freq_s1 == freq_window