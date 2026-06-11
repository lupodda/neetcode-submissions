from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        values = self.hashmap[key]
        left = 0
        right = len(values)-1
        res = ""
        # [(happy, 1), (sad, 3)]
        while left <= right:
            mid = (left+right)//2
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                left = mid+1
            else:
                right = mid-1

        return res

        
        
