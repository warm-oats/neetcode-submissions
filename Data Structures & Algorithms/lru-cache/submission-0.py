class Node:
    def __init__(self, key: int, val: int):
        self.next = self.prev = None
        self.key = key
        self.val = val

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])

            return self.cache[key].val

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

    def insert(self, node):
        prev = self.right.prev

        prev.next = node
        self.right.prev = node
        node.prev = prev
        node.next = self.right

    def remove(self, node):
        nxt = node.next
        prev = node.prev

        nxt.prev = prev
        prev.next = nxt
