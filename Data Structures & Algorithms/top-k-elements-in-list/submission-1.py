from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequences = defaultdict(int)

        for i, n in enumerate(nums):
            frequences[n] += 1
        
        sorted_freq = sorted(frequences.items(), key = lambda x: x[1], reverse = True)
        most_freq = [n for n, f in sorted_freq]

        return most_freq[:k]



        