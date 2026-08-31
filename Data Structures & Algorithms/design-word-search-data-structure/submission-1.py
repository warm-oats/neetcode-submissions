class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.end_of_word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
        self.store = []

    def addWord(self, word: str) -> None:
        curr_node = self.root

        for char in word:
            if char not in curr_node.children:
                new_char_node = TrieNode()
                curr_node.children[char] = new_char_node

            curr_node = curr_node.children[char]
        
        curr_node.end_of_word = True

        self.store.append(word)

    def search(self, word: str) -> bool:
        if '.' in word:
            return self.wildcard_search(word)

        curr_node = self.root

        for char in word:
            if char not in curr_node.children:
                return False
            
            curr_node = curr_node.children[char]

        return curr_node.end_of_word

    def wildcard_search(self, wildcard: str) -> bool:
        for word in self.store:
            index = 0
            recycle = False

            if len(wildcard) != len(word):
                continue

            while index < len(wildcard):
                if wildcard[index] != word[index] and wildcard[index] != '.':
                    recycle = True
                    break

                index += 1

            if recycle == False:
                return True

            recycle = False

        return False

        
        
