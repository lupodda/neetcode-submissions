class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for string in strs:
            encoded_string += str(len(string))+"-"+string

        return encoded_string

    def decode(self, s: str) -> List[str]:
        right = 0
        left = 0
        decoded_list = []

        while right < len(s):
            while s[right] != "-":
                right += 1

            # increase the right pointer until I find the delimiter -
            sting_length = int(s[left:right])
            substring = s[right+1:right+sting_length+1]
            left = right+sting_length+1
            right = right+sting_length+1
            decoded_list.append(substring)
            
        return decoded_list


        #loop over the string until you find the fist - 
        # extract the lenght of the string 
        # extract the substring from the index of the delimiter - to the index + the prev extracted num
        # append the substring to the decoded list
        
"""        ord(char)
        ["Hel-lo", "World"] -> "Hel-lo-World" -> ["Hel", "lo", "World"]
        s = [".","."] s.split("o")
        ["6Hel-lo", "World"] -> "7-6Hel-lo5-World" -> ["Hel", "lo", "World"]
"""