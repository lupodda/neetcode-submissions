class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            encoded_string += str(len(s))+"-"+s
        return encoded_string
    def decode(self, s: str) -> List[str]:
        decoded_list = []
        right, left = 0,0
        while right < len(s):
            while s[right] != "-":
                right +=1
            len_substring = int(s[left:right])
            start = right+1
            end = start+len_substring
            substring = s[start:end]
            decoded_list.append(substring)
            left,right = end, end
        return decoded_list

            
            
