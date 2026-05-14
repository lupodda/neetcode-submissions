class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""

        for s in strs:
            encoded_string += str(len(s)) + "-" + s

        return encoded_string
        #"5-Hello5-World"
    def decode(self, s: str) -> List[str]:
        res = []

        left = 0
        right = 0

        while left < len(s):
            while s[right] != "-":
                right += 1

            length = int(s[left:right])
            left = right+1
            right = left+length
            res.append(s[left:right])
            left = right

        return res
        


