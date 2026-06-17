class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap, self.cache = capacity, {}
        self.left = self.right = Node(0,0)
        self.left.next, self.right.prev = self.right, self.left
        
    def insert(self, node):
        prev = self.right.prev
        prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
        # Update the value of the existing node
            self.remove(self.cache[key])
        elif len(self.cache) == self.cap:
        # Remove the least recently used node
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        # Insert the new or updated node
        new_node = Node(key, value)
        self.insert(new_node)
        self.cache[key] = new_node
            
            
        
