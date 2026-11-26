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


# MAIN TAKEAWAYS:
# remember the for loop to process the elements at the same level in the queue
# remember to use the visited set, this avoids a lot of useless computations
# generating the neighbors on the fly using the close combinations is not very computationally heavy
# generating the graph on the fly takes a complexity of n*l^2 while genetating it before takes (n^2)*l ( much worse)
# return immediately after popping helps in dealing with the corrent number of transformations

#TIME AND SPACE COMPLEXITY:
# time: n*(l^2)
#space: 3*n*l -> n*l


