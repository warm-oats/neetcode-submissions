class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.end_of_word = False

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = set()

        for word in words:
            self.insert_word(word)
        
        def dfs(root: TrieNode, row: int, col: int, substr, prev_indices):
            if root.end_of_word:
                res.add(substr)
 
            if self.valid_adj(row - 1, col, board, prev_indices) and board[row - 1][col] in root.children:
                dfs(root.children[board[row - 1][col]], row - 1, col, substr + board[row - 1][col], prev_indices + [[row, col]])
            if self.valid_adj(row + 1, col, board, prev_indices) and board[row + 1][col] in root.children:
                dfs(root.children[board[row + 1][col]], row + 1, col, substr + board[row + 1][col], prev_indices + [[row, col]])
            if self.valid_adj(row, col - 1, board, prev_indices) and board[row][col - 1] in root.children:
                dfs(root.children[board[row][col - 1]], row, col - 1, substr + board[row][col - 1], prev_indices + [[row, col]])
            if self.valid_adj(row, col + 1, board, prev_indices) and board[row][col + 1] in root.children:
                dfs(root.children[board[row][col + 1]], row, col + 1, substr + board[row][col + 1], prev_indices + [[row, col]])

        for row in range(0, len(board)):
            for col in range(0, len(board[row])):
                char = board[row][col]

                if char in self.root.children:
                    dfs(self.root.children[char], row, col, char, [])

        return list(res)


    def valid_adj(self, row: int, col: int, board: List[List[str]], prev_indices) -> bool:
        res = True

        if row < 0 or col < 0:
            res = False
        if row >= len(board) or col >= len(board[0]):
            res = False
        if [row, col] in prev_indices:
            res = False

        return res

    def insert_word(self, word):
        curr_node = self.root

        for char in word:
            if char not in curr_node.children:
                curr_node.children[char] = TrieNode()

            curr_node = curr_node.children[char]

        curr_node.end_of_word = True

        