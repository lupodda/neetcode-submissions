from collections import defaultdict, Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq_t = Counter(t)
        freq_window = defaultdict(int)
        need, have = len(freq_t), 0
        start, end = 0,0
        length_min_window = float("inf")
        left = 0

        for right, char in enumerate(s):
            freq_window[char] += 1

            if freq_window[char] == freq_t[char]:
                have += 1

            while need == have:

                if right-left+1 < length_min_window:
                    start = left
                    end = right
                    length_min_window = end-start+1

                freq_window[s[left]] -= 1
                if s[left] in freq_t and freq_window[s[left]] < freq_t[s[left]]:
                    have -= 1

                left += 1

        return s[start:end+1] if length_min_window < float("inf") else ""

            




        