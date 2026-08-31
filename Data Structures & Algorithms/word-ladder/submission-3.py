class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        res = 0

        def backtrack(word: str, word_arr: List[str], count: int):
            nonlocal res

            if word == endWord:
                if res > 0:
                    res = min(res, count)
                else:
                    res = count
                return

            if not word_arr:
                return

            for i in range(len(word_arr)):
                diff_count = 0
                next_word = word_arr[i]

                for j in range(len(next_word)):
                    if word[j] != next_word[j]:
                        diff_count += 1

                if diff_count == 1:
                    backtrack(next_word, word_arr[0:i] + word_arr[i+1:], count + 1)

        backtrack(beginWord, wordList, 1)

        return res
                