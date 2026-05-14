from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        len_s1 = len(s1)
        len_s2 = len(s2)

        freq_s1 = defaultdict(int)
        for s in s1:
            freq_s1[s] += 1
        if len_s1 > len_s2:
            return False

        substring = defaultdict(int)
        for right in range(len_s2):
            if right-left+1 > len_s1:
                substring[s2[left]]-=1
                if substring[s2[left]] == 0:
                    del substring[s2[left]]
                left+=1
                
            substring[s2[right]] +=1
            print(substring)
            if freq_s1 == substring:
                return True
        return False




        