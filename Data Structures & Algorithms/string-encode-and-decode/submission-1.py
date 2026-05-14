class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string=""

        for string in strs:
            encoded_string+=str(len(string))+"-"+string

        return encoded_string


    def decode(self, s: str) -> List[str]:
        left = 0
        right = 0
        decoded_list = []

        while right < len(s):
            while s[right]!="-":
                right += 1
            len_substring=int(s[left:right])
            start = right+1
            end = start+len_substring
            substring=s[start:end]
            decoded_list.append(substring)
            left=end
            right=end
        return decoded_list







