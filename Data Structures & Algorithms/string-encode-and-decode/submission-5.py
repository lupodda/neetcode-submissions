class Solution:

    def encode(self, strs: List[str]) -> str:

        # ["ciao", "hello", "salut"]
        # "4#ciao"
        encoded_s = ""
        for s in strs:
            encoded_s += str(len(s)) + "#" + s

        return encoded_s

    def decode(self, s: str) -> List[str]:
        start, end = 0, 0
        res = []

        while end < len(s):
            while s[end] != "#":
                end+=1
            
            length = int(s[start:end])
            word = s[end+1:end+length+1]
            res.append(word)

            start = end = end+length+1

        return res



