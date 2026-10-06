class LRUCache:
    class Node:
        def __init__(self, key, val, next=None, prev=None):
            self.key = key
            self.val = val
            self.next = next
            self.prev = prev

    def __init__(self, capacity: int):
        self.left, self.right = self.Node(0, 0), self.Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left
        self.cacheMap = {}
        self.capacity = capacity
    
    def insert(self, node):
        node.prev = self.right.prev
        self.right.prev.next = node
        node.next = self.right
        self.right.prev = node
    
    def delete(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        result = -1
        if key in self.cacheMap:
            node = self.cacheMap[key]
            result = node.val
            self.delete(node)
            self.insert(node)
        
        return result

    def put(self, key: int, value: int) -> None:
        node = self.Node(key, value)
        if key in self.cacheMap:
            self.delete(self.cacheMap[key])
        self.insert(node)
        self.cacheMap[key] = node
        
        # now check if we have reached capacity
        if len(self.cacheMap) > self.capacity:
            # remove head
            del self.cacheMap[self.left.next.key]
            self.delete(self.left.next)
