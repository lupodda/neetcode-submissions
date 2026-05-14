from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window_frequences = defaultdict(int)
        left = 0
        res = 0

        for right in range(len(s)):
            window_frequences[s[right]]+=1

            while right-left+1 - max(window_frequences.values()) > k:
                window_frequences[s[left]]-=1
                left+=1

            res = max(res, right-left+1)

        return res


        