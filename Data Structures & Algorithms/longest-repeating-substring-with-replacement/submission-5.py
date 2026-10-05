class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left =0
        window_freq=defaultdict(int)
        max_length=0

        for right in range(len(s)):
            window_freq[s[right]]+=1

            while right-left+1 - max(window_freq.values())>k:
                window_freq[s[left]]-=1
                left+=1
            max_length=max(max_length, right-left+1)
        return max_length
            