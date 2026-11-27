from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue = deque([beginWord])
        visited = set({beginWord})
        wordSet = set(wordList)
        transformations = 1

        if beginWord == endWord:
            return 0

        while queue:
            for _ in range(len(queue)):
                current_word = queue.popleft()

                if current_word == endWord:
                    return transformations

                for i, char in enumerate(current_word):
                    for new_char in range(ord("a"), ord("z")+1):
                        possible_word = current_word[:i] + chr(new_char) + current_word[i+1:]

                        if possible_word in wordSet and possible_word not in visited:
                            queue.append(possible_word)
                            visited.add(possible_word)
            transformations += 1

        return 0


        