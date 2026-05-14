class Solution:
    def isValid(self, s: str) -> bool:
        """        s = '{[()]}[()]{()}'
        s = '{)[]}'

        1. if I find an open parethesis i add it to the stack
        2. if I find a closed parethesisand there is en element in the stack I check the last element of the stack
            if the last element of the stack is the corresponding opening elemet of the closed par. I remove it from the stack
           else return False
        3. if I go through all the string and at the my stack is empty I return True
        """
        
        stack = []
        mapping = {'}':'{', ')':'(', ']':'['}
        for symbol in s:
            if symbol in '{([':
                stack.append(symbol)
            if symbol in '}])':
                if stack and stack[-1] == mapping[symbol]:
                    stack.pop()
                else:
                    return False

        if not stack:
            return True
        else:
            return False


        