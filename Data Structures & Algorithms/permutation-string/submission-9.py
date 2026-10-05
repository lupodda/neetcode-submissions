from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        left = 0
        right = len(s1)

        freq_s1 = Counter(s1)
        freq_window_s2 = Counter(s2[left:right])

        while right < len(s2):
            if freq_s1 == freq_window_s2:
                return True

            freq_window_s2[s2[left]] -=1

            if freq_window_s2[s2[left]] == 0:
                del freq_window_s2[s2[left]]

            freq_window_s2[s2[right]] += 1

            left += 1
            right+=1

        return freq_s1 == freq_window_s2

        