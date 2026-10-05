class LRUCache:

    def __init__(self, capacity: int):
        self.lru_cache = {}
        self.capacity = capacity
        self.head = Node(0, None)
        self.tail = Node(0, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert(self, node):
        temp = self.tail.prev
        self.tail.prev = node
        node.next = self.tail
        node.prev = temp
        temp.next = node

    def delete(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def get(self, key: int) -> int:
        if key not in self.lru_cache:
            return -1

        node = self.lru_cache[key]
        self.delete(node)
        self.insert(node)
        return node.val
        
    def put(self, key: int, value: int) -> None:
        if key not in self.lru_cache:
            node = Node(key, value)
            self.insert(node)
            self.lru_cache[key]= node
            if len(self.lru_cache) > self.capacity:
                lru_node = self.head.next
                del self.lru_cache[lru_node.key]
                self.delete(lru_node)
        else:
            node = self.lru_cache[key]
            node.val = value
            self.delete(node)
            self.insert(node)

class Node:
    def __init__(self, key, val, prev= None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.key = key
        
