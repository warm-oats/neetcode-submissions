class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.end_of_word = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur_node = self.root

        for letter in word:
            if letter not in cur_node.children:
                cur_node.children[letter] = TrieNode()
            
            cur_node = cur_node.children[letter]
        
        cur_node.end_of_word = True

    def search(self, word: str) -> bool:
        cur_node = self.root

        for letter in word:
            if letter not in cur_node.children:
                return False

            cur_node = cur_node.children[letter]

        return cur_node.end_of_word

    def startsWith(self, prefix: str) -> bool:
        cur_node = self.root

        for letter in prefix:
            if letter not in cur_node.children:
                return False

            cur_node = cur_node.children[letter]

        return True
        