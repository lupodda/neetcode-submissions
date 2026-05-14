class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            match token:
                case "+":
                    right = int(stack.pop())
                    left = int(stack.pop())
                    stack.append(left + right)
                case "-":
                    right = int(stack.pop())
                    left = int(stack.pop())
                    stack.append(left - right)                
                case "*":
                    right = int(stack.pop())
                    left = int(stack.pop())
                    stack.append(left * right)
                case "/":
                    right = int(stack.pop())
                    left = int(stack.pop())
                    stack.append(int(left / right))
                case _:
                    stack.append(int(token))

        return stack.pop()