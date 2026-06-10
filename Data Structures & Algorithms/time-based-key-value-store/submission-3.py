from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.hash_map = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hash_map[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        values = self.hash_map[key]
        left = 0
        right = len(values)-1

        if not values or values[0][1] > timestamp:
            return ""
        while left < right:

            mid = ((left+right)//2)+1
            if values[mid][1] <= timestamp:
                left = mid
            else:
                right = mid-1

        return values[left][0]