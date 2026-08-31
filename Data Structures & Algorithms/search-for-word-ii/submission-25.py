class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.end_of_word = False

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res, visited_indices = set(), set()

        for word in words:
            self.insert_word(word)
        
        def dfs(root: TrieNode, row: int, col: int, substr = ''):
            if (row < 0 or col < 0
            or row >= len(board)
            or col >= len(board[row])
            or (row, col) in visited_indices
            or board[row][col] not in root.children):
                return None
            
            char = board[row][col]
            substr += char
            node = root.children[char]

            if node.end_of_word:
                res.add(substr)

            visited_indices.add((row, col))

            dfs(node, row + 1, col, substr)
            dfs(node, row - 1, col, substr)
            dfs(node, row, col - 1, substr)
            dfs(node, row, col + 1, substr)

            visited_indices.remove((row, col))

        for row in range(0, len(board)):
            for col in range(0, len(board[row])):
                dfs(self.root, row, col)

        return list(res)

    def insert_word(self, word):
        curr_node = self.root

        for char in word:
            if char not in curr_node.children:
                curr_node.children[char] = TrieNode()

            curr_node = curr_node.children[char]

        curr_node.end_of_word = True

        

        
        