class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.right = Node(None, 0)
        self.left = Node(None, 0)
        self.left.next = self.right
        self.right.prev = self.left
    
    def insert(self, node):
        prev = self.right.prev

        node.prev = prev
        node.next = self.right
        self.right.prev = node
        prev.next = node
    
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
        return node.val
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
        elif len(self.cache) == self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
            new_node = Node(key, value)
            self.insert(new_node)
            self.cache[key] = new_node

        else:
            new_node = Node(key, value)
            self.insert(new_node) 
            self.cache[key] = new_node



class Node:
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

        
# 1) implent a class node
# 2) in init use an hashmap as a cache anf store the capacity
# 3) implement insert adn remove node 
# 4) to get a value we simply use the hashmap
# 5) check if the cache is at capacity, remove the node on the left and we add the new element on the right
