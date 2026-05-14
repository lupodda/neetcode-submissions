class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        len_s1 = len(s1)
        len_s2 = len(s2)

        freq_s1 = [0]*26
        ord_a = ord("a")
        freq_window = [0]*26

        if len_s1 > len_s2:
            return False

        for s in s1:
            freq_s1[ord(s)-ord_a] += 1

        for right in range(len_s2):
            if right-left+1 > len_s1:
                freq_window[ord(s2[left])-ord_a] -= 1
                left+=1
                
            freq_window[ord(s2[right])-ord_a] +=1
            if freq_s1 == freq_window:
                return True
        return False




        