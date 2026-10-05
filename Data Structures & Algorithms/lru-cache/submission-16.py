class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def insert(self, node):
        prev = self.tail.prev
        prev.next = node
        self.tail.prev = node
        node.prev = prev
        node.next = self.tail        

    def get(self, key: int) -> int:
        if not key in self.cache:
            return -1
        
        # update the position of the node in the key
        # return the value of the node
        node = self.cache[key]
        self.remove(node)
        self.insert(node)

        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            #update the value
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.insert(node)
        else:
            # add the new element
            # check the capacity
            # in case remove the lru element (head)
            node = Node(key, value)
            self.insert(node)
            self.cache[key] = node
            if len(self.cache)>self.capacity:
                lru_node = self.head.next
                self.remove(lru_node)
                del self.cache[lru_node.key]

        
class Node:
    def __init__(self, key=0, val=0, prev = None, next = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next
        
