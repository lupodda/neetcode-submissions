from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = defaultdict(int)
        unique_elements = []
        for i, n in enumerate(nums):
            hash_map[n] += 1
        sorted_hash = dict(sorted(hash_map.items(), key=lambda item: item[1]))
        keys = list(sorted_hash.keys())
        for j in range(k):
            unique_elements.append(keys[len(keys)-j-1])

        return unique_elements


        