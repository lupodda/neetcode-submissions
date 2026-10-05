class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lru_cache = {}
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head
        
    def insert(self, node):
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node
        
    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def get(self, key: int) -> int:
        if key not in self.lru_cache:
            return -1
        
        node = self.lru_cache[key]
        self.remove(node)
        self.insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.lru_cache:
            node = self.lru_cache[key]
            node.val = value
            self.remove(node)
            self.insert(node)
        else:
            node = Node(key, value)
            self.lru_cache[key] = node
            self.insert(node)
            if len(self.lru_cache)> self.capacity:
                lru_node = self.head.next
                self.remove(lru_node)
                del self.lru_cache[lru_node.key]

class Node:
    def __init__(self, key = 0, val = 0, prev = None, next = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next    
        
