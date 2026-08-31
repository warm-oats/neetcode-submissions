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
        def dfs(j_index, root):
            curr_node = root

            for i in range(j_index, len(word)):
                char = word[i]

                if char == '.':
                    for child in curr_node.children.values():
                        if dfs(i + 1, child):
                            return True

                    return False
                else:
                    if char not in curr_node.children:
                        return False

                    curr_node = curr_node.children[char]

            return curr_node.end_of_word

        return dfs(0, self.root)



