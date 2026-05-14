from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window_frequences = defaultdict(int)
        max_window_len = 0
        left = 0

        for right in range(len(s)):
            window_frequences[s[right]]+=1

            while (right-left+1) - max(window_frequences.values()) > k:
                window_frequences[s[left]]-=1
                left+=1

            max_window_len = max(max_window_len, right-left+1)

        return max_window_len




        