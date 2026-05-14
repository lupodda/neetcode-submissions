from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        window_freq = defaultdict(int)
        max_length = 0

        for right in range(len(s)):
            while window_freq[s[right]] > 0:
                window_freq[s[left]]-=1
                left+=1
            window_freq[s[right]]+=1
            max_length = max(max_length, right-left+1)

        return max_length
        