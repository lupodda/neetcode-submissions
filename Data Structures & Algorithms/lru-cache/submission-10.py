class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(None, 0)
        self.tail = Node(None, 0)
        self.tail.prev = self.head
        self.head.next = self.tail

    def get(self, key: int) -> int:
        if not key in self.cache:
            return -1
        
        node = self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.remove(node)
            self.insert(node)
        else:
            node = Node(key, value)
            self.insert(node)
            self.cache[key] = node

            if len(self.cache) > self.capacity:
                lru_node = self.head.next
                self.remove(lru_node)
                del self.cache[lru_node.key]

    def insert(self, node):
        prev = self.tail.prev
        prev.next = node
        self.tail.prev = node
        node.next = self.tail
        node.prev = prev
    
    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

class Node:
    def __init__(self, key, value, prev = None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next
        
