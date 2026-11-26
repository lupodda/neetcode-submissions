from collections import defaultdict, deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue = deque([beginWord])
        wordSet = set(wordList)
        transformations = 1
        visited = set({beginWord})

        if beginWord == endWord:
            return 0 

        while queue:

            for _ in range(len(queue)):
                word = queue.popleft()

                if word == endWord:
                    return transformations
                    
                for i, c in enumerate(word):
                    for n in range(26):
                        possible_id = (ord(c) - ord('a') + n) %26
                        possible_c = chr(possible_id + ord('a'))
                        possible_word = word[:i]+possible_c+word[i+1:]

                        if possible_word in wordSet and possible_word not in visited:
                            queue.append(possible_word)
                            visited.add(possible_word)

            transformations += 1


        return 0



