class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_char = {}
        left = 0
        max_length = 0
        # s="pwwkew"

        for right, char in enumerate(s):
            if char in seen_char and seen_char[char] >= left:
                left = seen_char[char] + 1

            seen_char[char] = right
            max_length = max(max_length, right - left + 1)

        return max_length
             
                



        