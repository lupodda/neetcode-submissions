class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # initialize a stack
        # for all temperatures push the ith day in the stack 
        # while the temperature is less than the latest seen temprature pop it

        stack = []
        res = [0]*len(temperatures)

        for i,t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                res[stack[-1]] = i - stack[-1]
                stack.pop()

            stack.append(i)
        
        return res

        