from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_strs = defaultdict(list)

        for string in strs:
            sorted_str = "".join(sorted(string))

            grouped_strs[sorted_str].append(string)
        
        return list(grouped_strs.values())