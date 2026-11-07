class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = [0]*(len(nums)+1)
        hashmap = {}
        for i, num in enumerate(nums):
            prefix[i+1] = prefix[i]+num

        seen = defaultdict(int)
        seen[0] = 1
        count = 0
        for i in range(1, len(nums)+1):
            value = prefix[i]-k
            if value in seen:
                count += seen[value]
            seen[prefix[i]] += 1

        return count
            

        #[0,2,1,2,4]
        

    

