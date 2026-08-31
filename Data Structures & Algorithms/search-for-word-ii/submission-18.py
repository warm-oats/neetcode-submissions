class TrieNode:
    def __init__(self, val = None):
        self.children = defaultdict(TrieNode)
        self.end_of_word = False
        self.val = val

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

            adj_indices = self.get_adj(row, col, board, prev_indices)

            for adj_index in adj_indices:
                adj_char = board[adj_index[0]][adj_index[1]]

                if adj_char in root.children and tuple(adj_index) not in prev_indices:
                    prev = prev_indices
                    prev.add((row, col))

                    dfs(root.children[adj_char], adj_index[0], adj_index[1], substr + adj_char, prev)

        for row in range(0, len(board)):
            for col in range(0, len(board[row])):
                char = board[row][col]

                if char in self.root.children:
                    dfs(self.root.children[char], row, col, char, set())

        return list(res)


    def get_adj(self, row: int, col: int, board: List[List[str]], prev_indices) -> List[List[int]]:
        res = []

        if (row - 1) > -1 and (row - 1, col) not in prev_indices:
            res.append([row - 1, col])
        if (row + 1) < len(board) and (row + 1, col) not in prev_indices:
            res.append([row + 1, col])
        if (col - 1) > -1 and (row, col - 1) not in prev_indices:
            res.append([row, col - 1])
        if (col + 1) < len(board[0]) and (row, col + 1) not in prev_indices:
            res.append([row, col + 1])

        return res

    def insert_word(self, word):
        curr_node = self.root

        for char in word:
            if char not in curr_node.children:
                curr_node.children[char] = TrieNode(char)

            curr_node = curr_node.children[char]

        curr_node.end_of_word = True

        