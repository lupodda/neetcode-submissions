class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lru_cache = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert_node(self, node):
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node
    
    def remove_node(self, node):
        prev = node.prev
        next = node.next
        next.prev = prev
        prev.next = next

    def get(self, key: int) -> int:
        if key not in self.lru_cache:
            return -1

        node = self.lru_cache[key]
        self.remove_node(node)
        self.insert_node(node)
        return node.val

    def put(self, key: int, value: int) -> None:

        if key in self.lru_cache:
            node = self.lru_cache[key]
            node.val = value
            self.remove_node(node)
            self.insert_node(node)

        else:
            node = Node(key, value)
            self.lru_cache[key] = node
            self.insert_node(node)
            if len(self.lru_cache) > self.capacity:
                node = self.head.next
                self.remove_node(node)
                del self.lru_cache[node.key]

class Node:
    def __init__(self, key = 0, val = 0, prev = None, next = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next
        
