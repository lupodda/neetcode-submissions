class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(None, 0)
        self.tail = Node(None, 0)
        
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def insert(self, node):
        prev = self.tail.prev

        node.prev = prev
        prev.next = node
        node.next = self.tail
        self.tail.prev = node
    
    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            node.value = value
        else:
            new_node = Node(key, value)
            self.insert(new_node)
            self.cache[key] = new_node
            if len(self.cache) > self.capacity:
                lru_node = self.head.next
                self.remove(lru_node)
                del self.cache[lru_node.key]


class Node:
    def __init__(self, key, value, prev = None, next = None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next
        
