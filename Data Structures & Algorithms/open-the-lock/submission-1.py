from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        #Input: deadends = ["1000","0100","0010","0001"], target = "0000"
        deadends = set(deadends)

        start = "0000"

        if start in deadends:
            return -1

        queue = deque([start])
        visited = set({start})
        n_rotations = 0

        while queue:
            for _ in range(len(queue)):
                current = queue.popleft()

                if current == target:
                        return n_rotations

                for i, digit in enumerate(current):
                    digit = int(digit)

                    for possibility in (-1, 1):
                        current_copy = current[:i] + str((digit+possibility)%10) + current[i+1:]
                        if current_copy not in deadends and current_copy not in visited:
                            queue.append(current_copy)
                            visited.add(current_copy)

            n_rotations+=1

        return -1                
            
                






