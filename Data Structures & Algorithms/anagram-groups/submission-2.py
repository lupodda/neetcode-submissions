class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        anagrams =defaultdict(list)

        for string in strs:
            sorted_str = "".join(sorted(string))
            anagrams[sorted_str].append(string)
        return [val for key, val in anagrams.items()]