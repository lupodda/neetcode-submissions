from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)

        for i, word in enumerate(strs):
            sorted_word = "".join(sorted(word))

            if sorted_word in hash_map:
                hash_map[sorted_word].append(word)
            else:
                hash_map[sorted_word] = [word]
        
        return list(hash_map.values())
        