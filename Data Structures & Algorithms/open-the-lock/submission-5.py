class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        initial_lock = '0000'
        if initial_lock in deadends:
            return -1
        turns = 0
        begin = {initial_lock}
        end = {target}
        visited = set()
        while begin and end:
            if len(begin) > len(end):
                begin, end = end, begin
            next_level = set()
            for lock in begin:
                if lock in end:
                    return turns
                visited.add(lock)
                for i, wheel in enumerate(lock):
                    for option in (-1, 1):
                        digit = (int(wheel) + option) % 10
                        new_lock = lock[:i] + str(digit) + lock[i + 1:]
                        if new_lock not in visited and new_lock not in deadends:
                            next_level.add(new_lock)
            begin = next_level
            turns += 1
        return -1