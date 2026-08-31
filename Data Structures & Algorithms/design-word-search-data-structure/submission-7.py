class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.end_of_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr_node = self.root

        for char in word:
            if char not in curr_node.children:
                curr_node.children[char] = TrieNode()

            curr_node = curr_node.children[char]

        curr_node.end_of_word = True

    def search(self, word: str) -> bool:
        def dfs(word: str, curr_node: TrieNode) -> bool:
            if word == '':
                return curr_node.end_of_word

            if word[0] == '.':
                if len(curr_node.children.values()) == 0:
                    return False

                check = False

                for child in curr_node.children.values():
                    check = check or dfs(word[1:], child)

                return check
            elif word[0] not in curr_node.children:
                return False
            else:
                return dfs(word[1:], curr_node.children[word[0]])

        return dfs(word, self.root)

            
