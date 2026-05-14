class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lru_cache = {} #key = int, value = Node
        self.head = Node(None, 0)
        self.tail = Node(None, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def get(self, key: int) -> int:
        if key not in self.lru_cache:
            return -1

        node = self.lru_cache[key]
        self.remove(node)
        self.insert(node)
        return node.val

    def put(self, key: int, value: int):
        if key in self.lru_cache:
            node = self.lru_cache[key]
            node.val = value
            self.remove(node)
            self.insert(node)
        else:
            new_node = Node(key, value)
            self.insert(new_node)
            self.lru_cache[key] = new_node
            if len(self.lru_cache) > self.capacity:
                lru = self.head.next
                self.remove(lru)
                del self.lru_cache[lru.key]
        
    def insert(self, node):
        node.prev = self.tail.prev
        self.tail.prev.next = node
        node.next = self.tail
        self.tail.prev = node

    def remove(self, node):
        prev = node.prev
        next = node.next
        next.prev = prev
        prev.next = next        

class Node:
    def __init__(self, key, val, prev = None, next = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next
