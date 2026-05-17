class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            match token:
                case "+":
                    first = int(stack.pop())
                    second = int(stack.pop())
                    stack.append(first + second)
                case "-":
                    first = int(stack.pop())
                    second = int(stack.pop())
                    stack.append(second - first)
                case "*":
                    first = int(stack.pop())
                    second = int(stack.pop())
                    stack.append(first * second)
                case "/":
                    first = int(stack.pop())
                    second = int(stack.pop())
                    stack.append(int(second / first))
                case _:
                    stack.append(int(token))
        return stack.pop()
        