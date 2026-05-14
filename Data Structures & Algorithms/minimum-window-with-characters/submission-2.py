from collections import defaultdict, Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # count the frequences in t 
        # build the window

        freq_t = Counter(t)
        left = 0
        need, have = len(freq_t), 0
        freq_window = defaultdict(int)
        shortest_substring = s
        start, end = 0,0
        length_sunstring = float("inf")

        for right, char in enumerate(s):
            freq_window[char] +=1
            if freq_window[char] == freq_t[char]:
                have += 1

            while have == need:
                if right-left+1 <=  length_sunstring:
                    # shortest_substring = s[left:right+1]
                    start = left
                    end = right
                    length_sunstring = end-start+1


                freq_window[s[left]]-=1

                if s[left] in freq_t and freq_window[s[left]] < freq_t[s[left]]:
                    have -= 1
                
                left+=1


        return s[start:end+1] if length_sunstring < float("inf") else ""






        