import string

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        queue = deque()
        alphabet = list(string.ascii_lowercase)
        trans_count = 0

        queue.append(beginWord)

        if beginWord in wordList:
            wordList.remove(beginWord)

        def bfs(depth: int):
            if not queue:
                return

            for i in range(len(queue)):
                cur_word = queue.popleft()

                if cur_word == endWord:
                    nonlocal trans_count

                    if trans_count > 0:
                        trans_count = min(trans_count, depth)
                    else:
                        trans_count = depth

                    return

                for i in range(len(cur_word)):
                    for letter in alphabet:
                        trans_word = cur_word[:i] + letter + cur_word[i+1:]

                        if trans_word in wordList:
                            queue.append(trans_word)
                            wordList.remove(trans_word)
            
            bfs(depth + 1)

        bfs(1)

        return trans_count