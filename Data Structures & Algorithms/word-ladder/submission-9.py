import string

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        queue = deque()
        alphabet = list(string.ascii_lowercase)

        queue.append(beginWord)

        if beginWord in wordList:
            wordList.remove(beginWord)

        def bfs(depth: int):
            if not queue:
                return 0

            for i in range(len(queue)):
                cur_word = queue.popleft()

                if cur_word == endWord:
                    return depth

                for i in range(len(cur_word)):
                    for letter in alphabet:
                        trans_word = cur_word[:i] + letter + cur_word[i+1:]

                        if trans_word in wordList:
                            queue.append(trans_word)
                            wordList.remove(trans_word)
            
            return bfs(depth + 1)

        return bfs(1)