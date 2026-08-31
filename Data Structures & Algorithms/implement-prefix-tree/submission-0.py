class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.end_of_word = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr_node = self.root

        for char in word:
            if char not in curr_node.children.keys():
                new_char_node = TrieNode()
                curr_node.children[char] = new_char_node

            curr_node = curr_node.children[char]
        
        curr_node.end_of_word = True

    def search(self, word: str) -> bool:
        curr_node = self.root

        for char in word:
            if char in curr_node.children.keys():
                curr_node = curr_node.children[char]
            else:
                return False

        return curr_node.end_of_word

    def startsWith(self, prefix: str) -> bool:
        curr_node = self.root

        for char in prefix:
            if char in curr_node.children.keys():
                curr_node = curr_node.children[char]
            else:
                return False

        return True
        
        