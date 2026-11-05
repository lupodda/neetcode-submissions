class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for operation in operations:
            if operation == '+':
                record = stack[-1]+stack[-2]
                stack.append(record)
            elif operation == 'D':
                record = stack[-1]*2
                stack.append(record)
            elif operation == 'C':
                stack.pop()
            else:
                stack.append(int(operation))

        return sum(stack)

        
        