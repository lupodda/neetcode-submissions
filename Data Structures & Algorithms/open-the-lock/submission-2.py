from collections import defaultdict, deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        start = "0000"
        queue = deque([start])
        visited = set({})
        deadends = set(deadends)
        n_moves= 0
        if start in deadends:
            return -1

        if start == target:
            return n_moves

        while queue:
            n_moves += 1
            for _ in range(len(queue)):
                possible = queue.popleft()
                for i, num in enumerate(possible):
                    for increment in [-1, 1]:
                        move = (int(num)+increment)%10
                        combination = possible[:i]+str(move)+possible[i+1:]
                        if combination == target:
                            return n_moves
                        if combination not in deadends and combination not in visited:
                            queue.append(combination)
                            visited.add(combination)

        return -1




        