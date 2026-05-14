class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 1) return False if s1 is longer than s2
        # 2) count the frequences of charaters in s1 and s2 for a sunsting len(s1)
        # 3) count the number of matches and retrun True if matches == 26
        # 4) for the remaining characters in s2 slide a window of len s1
        # 5) update the number of matches based on the new encountered charracter
        # 6) return marches == 26 (True if we have found a substring, False otherwise)
        
        # 1)
        if len(s1)> len(s2):
            return False
        
        # 2)
        count_s1 = [0]*26
        count_s2 = [0]*26
        for i in range(len(s1)):
            count_s1[ord(s1[i])-ord("a")] += 1            
            count_s2[ord(s2[i])-ord("a")] += 1

        #3)
        matches = 0
        for i in range(26):
            if count_s1[i] == count_s2[i]:
                matches += 1

        left = 0
        for right in range(len(s1), len(s2)):
            if matches == 26: 
                return True
            
            index = ord(s2[right]) - ord("a")
            count_s2[index] += 1

            # check if with the new update we are marching the current index
            if count_s1[index] == count_s2[index]:
                matches+=1
            # else we chek if  with the new update we decreased the number of matches because maybe they were matching before
            elif count_s1[index] + 1 == count_s2[index]:
                # i check count_s1[index] + 1 because i have previously incremented count_s2[index]
                matches -=1
                # I dont check other condition because it means they were not matching before either
            
            index = ord(s2[left]) - ord("a")
            count_s2[index] -= 1
            if count_s1[index] == count_s2[index]:
                matches += 1
            elif count_s1[index]-1 == count_s2[index]:
                matches -= 1
            left+=1
            
        return matches == 26



        






