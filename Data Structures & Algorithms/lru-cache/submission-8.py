class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}
        self.head=Node(None, 0)
        self.tail=Node(None,0)
        self.head.next=self.tail
        self.tail.prev=self.head
    
    def insert(self, node):
        prev=self.tail.prev
        prev.next=node
        node.prev=prev
        node.next=self.tail
        self.tail.prev=node
    
    def remove(self, node):
        prev=node.prev
        next=node.next
        prev.next=next
        next.prev=prev
        
    def get(self, key: int) -> int:
        if key not in self.cache:
            return-1

        node=self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node=self.cache[key]
            node.val=value
            self.remove(node)
            self.insert(node)
        else:
            node=Node(key,value)
            self.cache[key]=node
            self.insert(node)

        if len(self.cache)>self.capacity:
            del self.cache[self.head.next.key]
            self.remove(self.head.next)


class Node:
    def __init__(self, key, value, prev=None, next=None):
        self.key=key
        self.val=value
        self.prev=prev
        self.next=next
  
        



































