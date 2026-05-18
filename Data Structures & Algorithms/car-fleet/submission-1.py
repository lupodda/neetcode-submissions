class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack=[]
        pairs = [(p,s) for s, p in zip(speed, position)]
        pairs.sort(reverse=True)

        for p,s in pairs:
            arrival_time= (target-p)/s
            stack.append(arrival_time)

            if len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()
        return len(stack)



        